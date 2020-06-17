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
        if self.dpix > self.dpiy:                                           # Max DPI of the created image
           self.dpimax = self.dpix                          
        else:
            self.dpimax = self.dpiy                        
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
            print('Set image path: ', self.path_in)
            return True
        else:
            self.path_in = './data/test.tiff'
            if os.path.isfile(path) != True:
                    print('File not found')
            elif (path.endswith('.tiff') or path.endswith('.tif') or path.endswith('.png') or path.endswith('.bmp') != True) :
                print('Wrong file ending')
            return False

    # def load_svg(self):
    #         """Load SVG"""
    #         self.img = pyvips.Image.svgload(self.path, dpi = self.dpimax)
    #         self.img = img.colourspace('b-w')
    #         self.img = img.invert()
    #         self.img = img.extract_band(1)

    #         self.imgloaded = True
    #         self.loadedimgpath = self.set_imagepath

    #         print('Load SVG:', self.path)

    # def load_bitmap(self):
    #         """Load Bitmap"""
    #         img = pyvips.Image.new_from_file(self.path)
    #         print('Load Bitmap:', self.path)
