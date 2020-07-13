import unittest
import ImageProcessing
import pint

class Image2Print(unittest.TestCase):

    def test0_calculate_printimage(self):
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.get_image_prop(
                                            path = "./data/Test.tiff",
                                            dpimax = 100
        )   


    def test1_calculate_printimage(self):
        #Test tiff loading, getting img properties, scale to defined value and arrange in printbed
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result1.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )

    def test2_calculate_printimage(self):
        #Test bg image
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result2.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [240, 240, 240]
        )   
        #self.assertEqual(img_prop, 145)

    def test3_calculate_printimage(self):
        #Test roatate
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result3.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 45, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [240, 240, 240]
        )   


    def test3_calculate_printimage(self):
        #Test roatate
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result3.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 100,
                                            offsety = 100, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )   

    def test4_calculate_printimage(self):
        #Test roatate and shift
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result4.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 45, 
                                            offsetx = 100,
                                            offsety = 100, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )   

    def test5_calculate_printimage(self):
        #Test scaling
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result5.tiff",
                                            sizex = 0.01, 
                                            sizey = 0.01, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )   

    def test6_calculate_printimage(self):
        #Test diff DPI res
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 300, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result6.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )   

    def test7_calculate_printimage(self):
        #Test diff DPI res2
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 300 , 
                                            dpiy = 200, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result7.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )   

    def test8_calculate_printimage(self):
        #Test diff DPI res2
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 200, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result8.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 45, 
                                            offsetx = 100,
                                            offsety = 100, 
                                            shrink = False, 
                                            bg =  [240, 240, 240]
        )   

    def test9_calculate_printimage(self):
        #Test overlapping
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 50, 
                                            dimy = 50, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result9.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )  

    def test10_calculate_printimage(self):
        #Test shrinking
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/Test.tiff",
                                            path_out = "./data/result10.tiff",
                                            sizex = 0.1, 
                                            sizey = 0.1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = True, 
                                            bg =  [255, 255, 255]
        )  

    def test11_calculate_printimage(self):
        #Test SVG Corel
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/test_corel.svg",
                                            path_out = "./data/result11.tiff",
                                            sizex = 1, 
                                            sizey = 1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )  

    def test12_calculate_printimage(self):
        #Test SVG Corel
        Image2Print = ImageProcessing.Image2Print()
        Image2Print.calculate_printimage(
                                            dpix = 100 , 
                                            dpiy = 100, 
                                            dimx = 300, 
                                            dimy = 300, 
                                            path_in = "./data/test_inkscape.svg",
                                            path_out = "./data/result12.tiff",
                                            sizex = 1, 
                                            sizey = 1, 
                                            rot = 0, 
                                            offsetx = 0,
                                            offsety = 0, 
                                            shrink = False, 
                                            bg =  [255, 255, 255]
        )  

if __name__ == '__main__':
    unittest.main()