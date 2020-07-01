import unittest
import ImageProcessing
import pint

#VARS
IMAGEPATH_EXISTING = "./data/Test.tiff"
IMAGEPATH_EXISTING_SVG_1 = "./data/test_corel.svg"
IMAGEPATH_EXISTING_SVG_2 = "./data/test_inkscape.svg"
IMAGEPATH_SYNTAX = "./data/Test.TIFF"
IMAGEPATH_WRONGENDING = "./data/x.jpg"
IMAGEPATH_NOTEXISTING = "./data/Tester.jpg"
IMAGEPATH_SAVE = "./data/result.tiff"
DPIX_1 = 100
DPIY_1 = 100
DPIX_2 = 100
DPIY_2 = 100
DPIX_3 = 300
DPIY_3 = 100
DIMX1 = 300                          # printbed dimension
DIMY1 = 300
OFFSETX1 = 100
OFFSETY1 = 100
ROT1 = 45 
SHRINK1 = False
BG1 =  [255, 255, 255]
SIZEX1 = 0.1                        # scaleing loaded img.
SIZEY1 = 0.1
class Image2Print(unittest.TestCase):

    def test1_calculate_printimage(self):
        #Test tiff loading, getting img properties, scale to defined value and arrange in printbed
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = DPIX_1 , 
                                            dpiy = DPIY_1, 
                                            dimx = DIMX1, 
                                            dimy = DIMY1, 
                                            path_in = IMAGEPATH_EXISTING,
                                            path_out = IMAGEPATH_SAVE,
                                            sizex = SIZEX1, 
                                            sizey = SIZEY1, 
                                            rot = ROT1, 
                                            offsetx = OFFSETX1,
                                            offsety = OFFSETY1, 
                                            shrink = SHRINK1, 
                                            bg = BG1
        )   


if __name__ == '__main__':
    unittest.main()