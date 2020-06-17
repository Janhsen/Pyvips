import unittest
import printimage
import pint


Image2Print = printimage.Image2Print()

class TestPrintImage(unittest.TestCase):

    def test_set_imagepath(self):
        #VARS
        IMAGEPATH_EXISTING = "./data/Test.tiff"
        IMAGEPATH_SYNTAX = "./data/Test.TIFF"
        IMAGEPATH_WRONGENDING = "./data/x.jpg"
        IMAGEPATH_NOTEXISTING = "./data/Tester.jpg"
        result = Image2Print.set_imagepath(IMAGEPATH_EXISTING)
        self.assertEqual(result,True)
        result = Image2Print.set_imagepath(IMAGEPATH_SYNTAX)
        self.assertEqual(result,True)
        result = Image2Print.set_imagepath(IMAGEPATH_WRONGENDING)
        self.assertEqual(result,False)
        result = Image2Print.set_imagepath(IMAGEPATH_NOTEXISTING)
        self.assertEqual(result,False)

    def test_calc_factors(self):
        #VARS
        ureg = pint.UnitRegistry()
        Image2Print.sizex = 1                                      # Scaling factor x
        Image2Print.sizey = 1                                      # Scaling factor y
        Image2Print.rot = 0                                        # Degree angle [°] to rotate the image 
        Image2Print.offsetx = 25.4 * (ureg.mm)                     # X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.offsety = 50.8 * (ureg.mm)                     # Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))
        Image2Print.shrink = False                                 # Shrink the printing image to smallest size Y | N
        Image2Print.bg = [255,255,255]                             # Background colour -> Fraunhofer RGB [23,156,125]'
        Image2Print.path_in = ""                                   # Image path of the input image
        Image2Print.path_out = ""                                  # Image path of the output image
        Image2Print.dpix = 100 * (ureg.count / ureg.inch)          # DPI in x direction
        Image2Print.dpiy = 200 * (ureg.count / ureg.inch)          # DPI in y direction
        Image2Print.dimx = 25.4 * (ureg.mm)                        # dimension [mm] in x direction
        Image2Print.dimy = 50.8 * (ureg.mm)                        # dimension [mm] in y direction
        Image2Print.calc_factors()
        self.assertEqual(Image2Print.printbedx_px , 100 *ureg.dimensionless)     # Test total pixel image x
        self.assertEqual(Image2Print.printbedy_px , 400 *ureg.dimensionless)     # Test total pixel image y
        self.assertEqual(Image2Print.offsetx_px , 100 *ureg.dimensionless)       # Test offset in pixel in y direction
        self.assertEqual(Image2Print.offsety_px , 400 *ureg.dimensionless)       # Test offset in pixel in y direction
        self.assertEqual(Image2Print.shrinkx , 2 * ureg.dimensionless)           # Test shrink factors
        self.assertEqual(Image2Print.shrinky , 1 * ureg.dimensionless)
        self.assertEqual(Image2Print.dpimax , 200 * (ureg.count / ureg.inch))
        Image2Print.dpix = 100 * (ureg.count / ureg.inch)          # DPI in x direction
        Image2Print.dpiy = 100 * (ureg.count / ureg.inch)          # DPI in y direction
        Image2Print.calc_factors()
        self.assertEqual(Image2Print.shrinkx , 1 * ureg.dimensionless)           # Test shrink factors
        self.assertEqual(Image2Print.shrinky , 1 * ureg.dimensionless)  
       
        Image2Print.dpix = 300 * (ureg.count / ureg.inch)          # DPI in x direction
        Image2Print.dpiy = 100 * (ureg.count / ureg.inch)          # DPI in y direction
        Image2Print.calc_factors()
        self.assertEqual(Image2Print.shrinkx , 1 * ureg.dimensionless)           # Test shrink factors
        self.assertEqual(Image2Print.shrinky , 3 * ureg.dimensionless)
        self.assertEqual(Image2Print.dpimax , 300 * (ureg.count / ureg.inch))

if __name__ == '__main__':
    unittest.main()