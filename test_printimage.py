import unittest
import printimage

IMAGEPATH_EXISTING = "./data/Test.tiff"
IMAGEPATH_SYNTAX = "./data/Test.TIFF"
IMAGEPATH_WRONGENDING = "./data/x.jpg"
IMAGEPATH_NOTEXISTING = "./data/Tester.jpg"

Image2Print = printimage.Image2Print()


class TestPrintImage(unittest.TestCase):

    def test_set_imagepath(self):
        result = Image2Print.set_imagepath(IMAGEPATH_EXISTING)
        self.assertEqual(result,True)
        result = Image2Print.set_imagepath(IMAGEPATH_SYNTAX)
        self.assertEqual(result,True)
        result = Image2Print.set_imagepath(IMAGEPATH_WRONGENDING)
        self.assertEqual(result,False)
        result = Image2Print.set_imagepath(IMAGEPATH_NOTEXISTING)
        self.assertEqual(result,False)

if __name__ == '__main__':
    unittest.main()