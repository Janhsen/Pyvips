import argparse
import os
import pathlib
import random
import pyvips
import pint

#UnitRegistry for unit conversion
ureg = pint.UnitRegistry()

x= (3 * ureg.mm / 4 * ureg.s)
print(x)

pixelx = 300 * ureg.count
# xres = 900 * (ureg.count / ureg.inch)
# xres.units = (ureg.count / ureg.mm)
# z= (pixelx / xres)
# print(z.name)


class Image2Print:

    def __init__(self):
        self.imgloaded = False
        self.loadedimgpath = ""

        self.dpimax = 1200
        self.sizex = 1
        self.sizey = 1
        self.rot = 0
        self.xoffset_mm = 0
        self.yoffset_mm = 0
        self.shrink = False 
        self.bg = [255,255,255]  # Fraunhofer RGB [23,156,125]'
        self.path_in = ""
        self.path_out = ""
        self.dpix = 0
        self.dpiy = 0
        self.dimx = 0
        self.dimy = 0


    # def calc_dots_per_printbed_direction(self, dim : float, or) -> int: 
    #     """Dots per printbed direction"""
    #     return round(dim * dpi_to_dpmm(self.) / 25.4)

    # def calc_factors(self):
    #     self.dpmmx = self.calc_dpmm(self.dpix)
    #     self.dpmmy = self.calc_dpmm(self.dpiy)

    #     self.printbedx = round(self.dimx * (self.dpix/25.4))
    #     self.printbedy = round(self.dimy *(self.dpiy/25.4))
    #     self.xoffset = int(self.xoffset_mm*(self.dpix/25.4))
    #     self.yoffset = int(self.yoffset_mm*(self.dpiy/25.4))
    #     if self.dpix >self.dpiy:
    #         self.dpimax = self.dpix
    #     else:
    #         self.dpimax = self.dpiy
    #     if (self.dpix/self.dpiy) > 1 :
    #         self.shrinkx = 1
    #         self.shrinky = self.dpix/self.dpiy
    #     if (dpiy/dpix) > 1 :
    #         self.shrinkx = dpiy/dpix
    #         self.shrinky = 1
    #     else:
    #         self.shrinkx = 1
    #         self.shrinky = 1
    #     self.dpimaxmm = self.dpimax*(1/25.40)
   
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
