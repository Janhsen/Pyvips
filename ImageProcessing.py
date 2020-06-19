import argparse
import os
import pathlib
import random
import pyvips
import pint

ureg = pint.UnitRegistry() 

class Image2Print:

    def __init__(self):
                                                                    # UnitRegistry for unit conversion
        self.loadedimgpath = ""                                     # Image path
        self.sizex = 1                                              # Scaling factor x
        self.sizey = 1                                              # Scaling factor y
        self.rot = 0                                                # Degree angle [°] to rotate the image 
        self.offsetx = 0 * (ureg.mm)                                # X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        self.offsety = 0 * (ureg.mm)                                # Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        self.shrink = False                                         # Shrink the printing image to smallest size Y | N
        self.bg = [255,255,255]                                     # Background colour -> Fraunhofer RGB [23,156,125]'
        self.path_in = ""                                           # Image path of the input image
        self.path_out = ""                                          # Image path of the output image
        self.dpix = 360 * (ureg.count / ureg.inch)                  # DPI in x direction
        self.dpiy = 360 * (ureg.count / ureg.inch)                  # DPI in y direction
        self.dimx = 0 * (ureg.mm)                                   # dimension [mm] in x direction
        self.dimy = 0 * (ureg.mm)                                   # dimension [mm] in y direction

    def calc_factors(self): 
        self.printbedx_px = self.dimx * self.dpix                           # Printbed pixel in x direction
        self.printbedx_px = round(self.printbedx_px.to_reduced_units())
        self.printbedy_px = self.dimy * self.dpiy                           # Printbed pixel in y direction
        self.printbedy_px = round(self.printbedy_px.to_reduced_units())
        self.offsetx_px = self.offsetx * self.dpix                          # Offset in pixel in x direction
        self.offsetx_px = round(self.offsetx_px.to_reduced_units())
        self.offsety_px = self.offsety * self.dpiy                          # Offset in pixel in y direction
        self.offsety_px = round(self.offsety_px.to_reduced_units())
        self.dpmmx = self.dpix.to(ureg.count / ureg.mm)
        self.dpmmy = self.dpiy.to(ureg.count / ureg.mm)
        if self.dpix > self.dpiy:                                           # Max DPI of the created image
           self.dpimax = self.dpix  
           self.dpmmmax = self.dpimax.to(ureg.count / ureg.mm)                       
        else:
            self.dpimax = self.dpiy     
            self.dpmmmax = self.dpimax.to(ureg.count / ureg.mm)                  
        if (self.dpix/self.dpiy) > 1 :                                      # Shrinking factors
            self.shrinkx = 1 * ureg.dimensionless
            self.shrinky = self.dpix/self.dpiy
        elif (self.dpiy/self.dpix) > 1 :
            self.shrinkx = self.dpiy/self.dpix
            self.shrinky = 1 * ureg.dimensionless
        else:
            self.shrinkx = 1 * ureg.dimensionless
            self.shrinky = 1 * ureg.dimensionless
   
    def set_imagepath(self, path :str = './data/test.tiff'):
        """Set image path (*.tiff,*.tif,*.png, *.bmp, *.svg)"""
        path = path.lower()
        if ((path.endswith('.tiff') or path.endswith('.tif') or path.endswith('.png') or path.endswith('.bmp') or path.endswith('.svg') ) and os.path.exists(path)) and os.path.isfile(path):
            self.path_in = path
            print('\nSet image path: ', self.path_in)
            return True
        else:
            self.path_in = './data/test.tiff'
            if os.path.isfile(path) != True:
                    print('File not found')
            elif (path.endswith('.tiff') or path.endswith('.tif') or path.endswith('.png') or path.endswith('.bmp') != True) :
                print('\nWrong file ending')
            return False

    def load_svg(self):
        if self.path_in != '' :
                """Load SVG"""
                print ('\nLoad SVG:', self.path_in),
                self.img = pyvips.Image.svgload(self.path_in, dpi = self.dpimax.magnitude)
                self.img = self.img.colourspace('b-w')
                self.img = self.img.invert()
                self.img = self.img.extract_band(1)
                print ('\nPixel width:', self.img.width, '\nPixel height:', self.img.height, '\nDPIx:', round(self.img.xres/(1/25.40),3), '\nDPIy:', round(self.img.yres/(1/25.40),3),'\n'), 
                self.buffer = self.img.tiffsave_buffer(xres = self.dpmmy.magnitude, yres = self.dpmmy.magnitude)
                self.img = pyvips.Image.tiffload_buffer(self.buffer)
                
                return True
        else:
                print ('\nNo image loaded')
                return False

    def load_bitmap(self):
        if self.path_in != '' :
            """Load Bitmap"""
            self.img = pyvips.Image.new_from_file(self.path_in)
            print ('\nLoad bitmap:', self.path_in),
            self.img = pyvips.Image.new_from_file(self.path_in)
            print ('\nwidth:', self.img.width, '\nheight:', self.img.height, '\nDPIx:', round(self.img.xres/(1/25.40),3), '\nDPIy:', round(self.img.yres/(1/25.40),3)), 
            self.scalex = round((self.img.xres / self.dpmmmax.magnitude),7)
            self.scaley = round((self.img.yres / self.dpmmmax.magnitude),7) 
            print ('\nResize org. image x:', 1/self.scalex, 'y:', 1/self.scaley)
            if self.scalex >= self.scaley :
                self.img = self.img.resize((1/self.scalex),vscale = (1/(self.scaley)))
            else:
                self.img = self.img.resize((1/self.scalex),vscale = (self.scaley))
            self.buffer = self.img.tiffsave_buffer(xres = self.dpmmx.magnitude, yres = self.dpmmy.magnitude)
            self.img = pyvips.Image.tiffload_buffer(self.buffer)
            return True
        else:
            print ('\nNo image loaded')
            return False

    def calc_image(self):  
        self.img = self.img.colourspace('b-w')
        self.printbed = self.img.extract_band(0)
        self.scalex = round((self.img.xres/self.dpmmmax.magnitude),7)*self.sizex
        self.scaley = round((self.img.yres/self.dpmmmax.magnitude),7)*self.sizey
        print ('Rescale image for DPIx and DPIy x:', self.scalex, 'y:',self.scaley)
        if self.scalex >= self.scaley :
            self.img = self.img.resize(self.scalex,vscale = (self.scaley))
        else:
            self.img = self.img.resize(self.scalex,vscale = (1/(self.scaley)))
        
        print ('\nwidth_resize:', self.img.width, '\nheight_resize:', self.img.height, '\nDPIx_resize:', round(self.img.xres/(1/25.40),3), '\nDPIy_resize:', round(self.img.yres/(1/25.40),3)), 
        print ('\nRotate', self.rot, '°') 
        self.img = self.img.rotate(self.rot, background =self.bg )
        
        if self.shrink == True:
            if (self.img.width + self.offsetx_px) < self.self.printbedx_px :
                self.self.printbedx_px = (self.img.width + self.offsetx_px)
            if (self.img.height + self.offsety_px) < self.self.printbedy_px :
                self.self.printbedy_px = (self.img.height + self.offsety_px)  

        print ('Create printbed bounding') 
        self.printbed_px = pyvips.Image.black(self.printbedx_px, self.printbedy_px)
        
        self.printbed_px = self.printbed_px.ifthenelse([0,0,0],self.bg)
        if self.bg == [255,255,255]:
            self.printbed = self.printbed.colourspace('b-w')
        print ('Merge images with pixel offset X=', self.offsetx_px,'and Y=', self.offsety_px)
        self.offsety_px = self.printbedy_px - self.img.height - self.offsety.magnitude
        self.printbed = self.printbed.insert(self.img, self.offsetx_px.magnitude, self.offsety_px.magnitude)
        print ('Convert to B&W') 
        #Create Printimage
        print ('Print image:', self.path_out,  '\n\nwidth_print:', self.printbed.width, '\nheight_print:', self.printbed.height, '\nDPIx_print:', self.dpmmx.magnitude/(1/25.40), '\nDPIy_print:', self.dpmmy.magnitude/(1/25.40)), 
        self.printbed.tiffsave(self.path_out, squash = True, xres = self.dpmmx.magnitude, yres = self.dpmmy.magnitude, compression = 'deflate')
        print ('\n####     Done     ####\n'), 

    def get_image_prop(self): 
        self.img_width_px = self.img.width
        self.img_height_px = self.img.height
        self.img_dpmmx = self.img.xres
        self.img_dpmmy = self.img.yres
        self.img_width_mm = self.img.width/self.img.xres
        self.img_height_mm = self.img.height/self.img.yres
        self.img_dpix = self.img.xres/(1/25.40)
        self.img_dpiy = self.img.yres/(1/25.40)
        print('Image width in pixel', self.img_width_px)
        print('Image height in pixel', self.img_height_px)
        print('Image width in mm', self.img_width_mm)
        print('Image height in mm', self.img_height_mm)
        print('Image DPI in X direction', self.img_dpix)
        print('Image DPI in > direction', self.img_dpiy)