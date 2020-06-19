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
DPIY_1 = 200
DPIX_2 = 100
DPIY_2 = 100
DPIX_3 = 300
DPIY_3 = 100
DIMX = 125.4
DIMY = 150.8
OFFSETX = 0
OFFSETY = 0
ROT = 0
SHRINK = True
BG =  [240, 240, 240]
SIZEX = 1
SIZEY = 1
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