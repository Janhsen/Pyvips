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
DPIX_1 = 300
DPIY_1 = 300
DPIX_2 = 100
DPIY_2 = 100
DPIX_3 = 300
DPIY_3 = 100
DIMX = 300
DIMY = 300
OFFSETX = 100
OFFSETY = 100
ROT = 0
SHRINK = False
BG =  [255, 255, 255]
SIZEX = 0.1
SIZEY = 0.1
class Image2Print(unittest.TestCase):

    def test1_calculate_printimage(self):
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
        dpix = DPIX_1 , 
        dpiy = DPIY_1, 
        dimx = DIMX, 
        dimy = DIMY, 
        path_in = IMAGEPATH_EXISTING,
        path_out = IMAGEPATH_SAVE,
        sizex = SIZEX, 
        sizey = SIZEY, 
        rot = ROT, 
        offsetx = OFFSETX,
        offsety = OFFSETY, 
        shrink = SHRINK, 
        bg = BG
        )   

if __name__ == '__main__':
    unittest.main()