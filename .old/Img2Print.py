
import os
import sys
import random
import argparse
import pyvips

#Phrasing of inputs 
#Example:  Img2Print.py --path_in='./data/test.tiff' --path_out './data/result.tiff' --dpix 100 --dpiy 100 --dimx 1000 --dimy 1000 --bg 255 255 255 --rot 45  --offx 10 --offy 10

parser = argparse.ArgumentParser(description='Process SVGs and Bitmaps for printing')
parser.add_argument("--path_in", required=True, type = str,
 	help="path to input image")
parser.add_argument("--path_out", required=True, type = str,
 	help="path to output image")
parser.add_argument("--dpix", required=True, type = int,
 	help="dpi in X direction of the image")
parser.add_argument("--dpiy", required=True, type = int,
 	help="dpi in Y direction of the image")
parser.add_argument("--dimx" , required=True, type = float,
 	help="x dimensions of the printbed in mm")   
parser.add_argument("--dimy" ,required=True, type = float,
 	help="y size of the printbed in mm") 
parser.add_argument("--sizex" , type = float,
 	help="x resize factor in percent to org. image") 
parser.add_argument("--sizey" , type = float,
 	help="y resize factor in percent to org. image") 
parser.add_argument("--rot", type = float,
 	help="rotation angle in °")
parser.add_argument("--offx" , type = float,
 	help="x offset in mm")   
parser.add_argument("--offy" , type = float,
 	help="y offset in mm") 
parser.add_argument("--shrink" , type = bool,
 	help="shrink the printing image to smallest size") 
parser.add_argument("--bg" , nargs='+', type=int,
 	help="Background colour indicating printbed") 
inputs = parser.parse_args()

#Hand over Input arguments
path_in = inputs.path_in
path_out = inputs.path_out
dpix = inputs.dpix
dpiy = inputs.dpiy
dimx = inputs.dimx
dimy = inputs.dimy

if inputs.sizex is not None:
    sizex= inputs.sizex
else:
    sizex = 1
if inputs.sizey is not None:
    sizey= inputs.sizex
else:
    sizey = 1
if inputs.rot is not None:
    rot= inputs.rot
else:
    rot = 0
if inputs.offx is not None:
    xoffset_mm= inputs.offx
else:
    xoffset_mm = 0
if inputs.offy is not None:
    yoffset_mm= inputs.offy
else:
    yoffset_mm = 0 
if inputs.shrink is not None:
    shrink= inputs.shrink
else:
    shrink = False 
if inputs.bg is not None:
    bg= inputs.bg
else:
    bg = [255,255,255]  # Fraunhofer RGB [23,156,125]'

#Calculate Vars
imagefound = False
path_in= path_in.lower()
path_out = path_out.lower()
dpmmx = dpix*(1/25.40)
dpmmy = dpiy*(1/25.40)
printbedx = round(dimx * (dpix/25.4))
printbedy = round(dimy *(dpiy/25.4))
xoffset = int(xoffset_mm*(dpix/25.4))
yoffset = int(yoffset_mm*(dpiy/25.4))
if dpix >dpiy:
    dpimax = dpix
else:
    dpimax = dpiy
if (dpix/dpiy) > 1 :
    shrinkx = 1
    shrinky = dpix/dpiy
if (dpiy/dpix) > 1 :
    shrinkx = dpiy/dpix
    shrinky = 1
else:
    shrinkx = 1
    shrinky = 1
dpimaxmm =dpimax*(1/25.40)

print ('\n####     Start     ####'), 

#Load image
if path_in.endswith('.svg') and os.path.isfile(path_in):
    print ('\nLoad SVG:', path_in), 
    img = pyvips.Image.svgload(path_in, dpi = dpimax)
    img = img.colourspace('b-w')
    img = img.invert()
    img = img.extract_band(1)
    print ('Render SVG with DPI:',dpimax), 
    #image has to be buffers -> else rotate slow
    print ('\nwidth:', img.width, '\nheight:', img.height, '\nDPIx:', round(img.xres/(1/25.40),3), '\nDPIy:', round(img.yres/(1/25.40),3),'\n'), 
    buffer = img.tiffsave_buffer(xres = dpmmx, yres = dpmmy)
    img = pyvips.Image.tiffload_buffer(buffer)
    imagefound = True

if ((path_in.endswith('.tiff') or path_in.endswith('.tif') or path_in.endswith('.png') or path_in.endswith('.bmp') ) and os.path.isfile(path_in))and os.path.isfile(path_in):
    print ('\nLoad bitmap:', path_in),
    img = pyvips.Image.new_from_file(path_in)
    print ('\nwidth:', img.width, '\nheight:', img.height, '\nDPIx:', round(img.xres/(1/25.40),3), '\nDPIy:', round(img.yres/(1/25.40),3)), 
    scalex = round((img.xres/dpimaxmm),7)
    scaley = round((img.yres/dpimaxmm),7)
    print ('\nResize org. image x:', 1/scalex, 'y:', 1/scaley)
    if scalex >= scaley :
        img = img.resize((1/scalex),vscale = (1/(scaley)))
    else:
        img = img.resize((1/scalex),vscale = (scaley))
    buffer = img.tiffsave_buffer(xres = dpmmx, yres = dpmmy)
    img = pyvips.Image.tiffload_buffer(buffer)
    imagefound = True

if imagefound == True:
    img = img.colourspace('b-w')

    printbed = img.extract_band(0)
    scalex = round((img.xres/dpimaxmm),7)*sizex
    scaley = round((img.yres/dpimaxmm),7)*sizey
    print ('Rescale image for DPIx and DPIy x:', scalex, 'y:',scaley)
    if scalex >= scaley :
        img = img.resize(scalex,vscale = (scaley))
    else:
        img = img.resize(scalex,vscale = (1/(scaley)))
    
    #Debug
    print('img.width', img.width)
    print('img.height', img.height)


    print ('\nwidth_resize:', img.width, '\nheight_resize:', img.height, '\nDPIx_resize:', round(img.xres/(1/25.40),3), '\nDPIy_resize:', round(img.yres/(1/25.40),3)), 
    print ('\nRotate', rot, '°') 
    img = img.rotate(rot, background =bg )
    
    if shrink == True:
        if (img.width + xoffset) < printbedx :
            printbedx = (img.width + xoffset)
        if (img.height + yoffset) < printbedy :
            printbedy = (img.height + yoffset)  
      
    print ('Create printbed bounding') 
    printbed = pyvips.Image.black(printbedx, printbedy)
    
    printbed = printbed.ifthenelse([0,0,0],bg)
    if bg == [255,255,255]:
        printbed = printbed.colourspace('b-w')
    print ('Merge images with pixel offset X=', xoffset,'and Y=', yoffset)
    yoffset = printbedy - img.height - yoffset
    printbed = printbed.insert(img, xoffset, yoffset)
    print ('Convert to B&W') 
    #Create Printimage
    print ('Print image:', path_out,  '\n\nwidth_print:', printbed.width, '\nheight_print:', printbed.height, '\nDPIx_print:', dpmmx/(1/25.40), '\nDPIy_print:', dpmmy/(1/25.40)), 
    printbed.tiffsave(path_out, squash = True, xres = dpmmx, yres = dpmmy, compression = 'deflate')
    print ('\n####     Done     ####\n'), 
else:
    print ('\nError loading image\n'), 
    print ('\n####     Done     ####\n'), 
