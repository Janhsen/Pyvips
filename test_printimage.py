import unittest
import printimage
import pint

#VARS
IMAGEPATH_EXISTING = "./data/Test.tiff"
IMAGEPATH_EXISTING_SVG = "./data/test.svg"
IMAGEPATH_SYNTAX = "./data/Test.TIFF"
IMAGEPATH_WRONGENDING = "./data/x.jpg"
IMAGEPATH_NOTEXISTING = "./data/Tester.jpg"
IMAGEPATH_SAVE = "./data/result.tiff"
DPIX_1 = 100
DPIY_1 = 200
DPIX_2 = 100
DPIY_2 = 100
DPIX_3 = 300
DPIY_3 = 100
DIMX = 25.4
DIMY = 50.8
OFFSETX = 25.4
OFFSETY = 50.8


class TestPrintImage(unittest.TestCase):

    def test_set_imagepath(self):
        Image2Print = printimage.Image2Print()
        result = Image2Print.set_imagepath(IMAGEPATH_EXISTING)
        self.assertEqual(result,True)
        result = Image2Print.set_imagepath(IMAGEPATH_SYNTAX)
        self.assertEqual(result,True)
        result = Image2Print.set_imagepath(IMAGEPATH_WRONGENDING)
        self.assertEqual(result,False)
        result = Image2Print.set_imagepath(IMAGEPATH_NOTEXISTING)
        self.assertEqual(result,False)

    def test_calc_factors(self):
        Image2Print = printimage.Image2Print()
        #VARS
        ureg = pint.UnitRegistry()
        Image2Print.sizex = 1                                      # Scaling factor x
        Image2Print.sizey = 1                                      # Scaling factor y 
        Image2Print.offsetx = OFFSETX * (ureg.mm)                     # X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.offsety = OFFSETY * (ureg.mm)                     # Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.dpix = DPIX_1 * (ureg.count / ureg.inch)          # DPI in x direction
        Image2Print.dpiy = DPIY_1 * (ureg.count / ureg.inch)          # DPI in y direction
        Image2Print.dimx = DIMX * (ureg.mm)                        # dimension [mm] in x direction
        Image2Print.dimy = DIMY * (ureg.mm)                        # dimension [mm] in y direction
        Image2Print.calc_factors()
        self.assertEqual(Image2Print.printbedx_px , 100 *ureg.dimensionless)     # Test total pixel image x
        self.assertEqual(Image2Print.printbedy_px , 400 *ureg.dimensionless)     # Test total pixel image y
        self.assertEqual(Image2Print.offsetx_px , 100 *ureg.dimensionless)       # Test offset in pixel in y direction
        self.assertEqual(Image2Print.offsety_px , 400 *ureg.dimensionless)       # Test offset in pixel in y direction
        self.assertEqual(Image2Print.shrinkx , 2 * ureg.dimensionless)           # Test shrink factors
        self.assertEqual(Image2Print.shrinky , 1 * ureg.dimensionless)
        self.assertEqual(Image2Print.dpimax , 200 * (ureg.count / ureg.inch))
        Image2Print.dpix = DPIX_2 * (ureg.count / ureg.inch)          # DPI in x direction
        Image2Print.dpiy = DPIY_2 * (ureg.count / ureg.inch)          # DPI in y direction
        Image2Print.calc_factors()
        self.assertEqual(Image2Print.shrinkx , 1 * ureg.dimensionless)           # Test shrink factors
        self.assertEqual(Image2Print.shrinky , 1 * ureg.dimensionless)  
        Image2Print.dpix = DPIX_3 * (ureg.count / ureg.inch)          # DPI in x direction
        Image2Print.dpiy = DPIY_3 * (ureg.count / ureg.inch)          # DPI in y direction
        Image2Print.calc_factors()
        self.assertEqual(Image2Print.shrinkx , 1 * ureg.dimensionless)           # Test shrink factors
        self.assertEqual(Image2Print.shrinky , 3 * ureg.dimensionless)
        self.assertEqual(Image2Print.dpimax , 300 * (ureg.count / ureg.inch))

    def test_load_svg(self):
        Image2Print = printimage.Image2Print()
        ureg = pint.UnitRegistry()
        Image2Print.sizex = 1                                      # Scaling factor x
        Image2Print.sizey = 1                                      # Scaling factor y 
        Image2Print.offsetx = OFFSETX * (ureg.mm)                  # X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.offsety = OFFSETY * (ureg.mm)                  # Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.dpix = DPIX_1 * (ureg.count / ureg.inch)       # DPI in x direction
        Image2Print.dpiy = DPIY_1 * (ureg.count / ureg.inch)       # DPI in y direction
        Image2Print.dimx = DIMX * (ureg.mm)                        # dimension [mm] in x direction
        Image2Print.dimy = DIMY * (ureg.mm)                        # dimension [mm] in y direction

        Image2Print.set_imagepath(path = IMAGEPATH_EXISTING_SVG)
        Image2Print.calc_factors()
        result = Image2Print.load_svg()
        Image2Print.get_image_prop()
        self.assertEqual(result,True)
        
    def test_load_bitmap(self):
        Image2Print = printimage.Image2Print()
        ureg = pint.UnitRegistry()
        Image2Print.sizex = 1                                      # Scaling factor x
        Image2Print.sizey = 1                                      # Scaling factor y 
        Image2Print.offsetx = OFFSETX * (ureg.mm)                  # X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.offsety = OFFSETY * (ureg.mm)                  # Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.dpix = DPIX_1 * (ureg.count / ureg.inch)       # DPI in x direction
        Image2Print.dpiy = DPIY_1 * (ureg.count / ureg.inch)       # DPI in y direction
        Image2Print.dimx = DIMX * (ureg.mm)                        # dimension [mm] in x direction
        Image2Print.dimy = DIMY * (ureg.mm)                        # dimension [mm] in y direction

        Image2Print.set_imagepath(path = IMAGEPATH_EXISTING)
        Image2Print.calc_factors()
        result = Image2Print.load_bitmap()
        Image2Print.get_image_prop()
        self.assertEqual(result,True)
        self.assertEqual(Image2Print.scalex,0.9, 1)
        self.assertEqual(Image2Print.scaley,0.9, 1)

    def test_calc_image(self):
        Image2Print = printimage.Image2Print()
        ureg = pint.UnitRegistry()
        Image2Print.sizex = 1                                      # Scaling factor x
        Image2Print.sizey = 1                                      # Scaling factor y 
        Image2Print.offsetx = OFFSETX * (ureg.mm)                  # X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.offsety = OFFSETY * (ureg.mm)                  # Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.dpix = DPIX_1 * (ureg.count / ureg.inch)       # DPI in x direction
        Image2Print.dpiy = DPIY_1 * (ureg.count / ureg.inch)       # DPI in y direction
        Image2Print.dimx = DIMX * (ureg.mm)                        # dimension [mm] in x direction
        Image2Print.dimy = DIMY * (ureg.mm)                        # dimension [mm] in y direction
        Image2Print.path_out = IMAGEPATH_SAVE

        Image2Print.set_imagepath(path = IMAGEPATH_EXISTING)
        Image2Print.calc_factors()
        Image2Print.load_bitmap()
        Image2Print.calc_image()

if __name__ == '__main__':
    unittest.main()