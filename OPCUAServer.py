import sys
sys.path.insert(0, "..")
import time
import logging
import ImageProcessing
from opcua import ua, Server, uamethod

if __name__ == "__main__":

    # setup server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/fraunhoferipa/server/")
    server.set_server_name("Fraunhofer OpcUa Server")
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

    # setup namespace
    uri = "http://ipa.fraunhofer.de"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    ImageProcessing = objects.add_object(idx, "stImageProcessing")
    CalculatePrintimage = ImageProcessing.add_object(idx, "stCalculatePrintimage")
    CalculatePrintimageIn = CalculatePrintimage.add_object(idx, "stIn")
    CalculatePrintimageOut = CalculatePrintimage.add_object(idx, "stOut")
    GetImageProperties = ImageProcessing.add_object(idx, "stGetImageProperties")

    ExecuteCalculatePrintimage = CalculatePrintimage.add_variable(idx, "xExecute", False) 
    path_in = CalculatePrintimageIn.add_variable(idx, "sPath_in", "./data/Test.tiff")
    path_in.set_writable()
    path_out = CalculatePrintimageIn.add_variable(idx, "sPath_out", "./data/result.tiff")
    path_out.set_writable()
    dpix = CalculatePrintimageIn.add_variable(idx,"iDpiX", 100)
    dpix.set_writable()
    dpiy = CalculatePrintimageIn.add_variable(idx, "iDpiY", 100)
    dpiy.set_writable()
    dimx = CalculatePrintimageIn.add_variable(idx, "rDimX", 300.0)
    dimx.set_writable()
    dimy = CalculatePrintimageIn.add_variable(idx, "rDimY", 300.0)
    dimy.set_writable()
    offsetx = CalculatePrintimageIn.add_variable(idx, "rOffsetX", 0.0)
    offsetx.set_writable()
    offsety = CalculatePrintimageIn.add_variable(idx, "rOffsetY", 0.0)
    offsety.set_writable()
    rot = CalculatePrintimageIn.add_variable(idx, "rRot", 0.0)
    rot.set_writable()
    shrink = CalculatePrintimageIn.add_variable(idx, "xShrink", True)
    shrink.set_writable()
    bg =  CalculatePrintimageIn.add_variable(idx, "arrBG", [255, 255, 255])
    bg.set_writable()
    sizex = CalculatePrintimageIn.add_variable(idx, "rSizeX", 1.0)
    sizex.set_writable()
    sizey = CalculatePrintimageIn.add_variable(idx, "rSizeX", 1.0)
    sizey.set_writable()

    ExecuteGetImageProperties = GetImageProperties.add_variable(idx, "xExecute", False)
    path = GetImageProperties.add_variable(idx, "path", "./data/Test.tiff")
    path.set_writable()
    dpimax = GetImageProperties.add_variable(idx, "dpimax", 100)
    dpimax.set_writable()

    # starting!
    server.start()

    try:
        while True:
            time.sleep(0.05)
            if (ExecuteCalculatePrintimage==True):
                Image2Print = ImageProcessing.Image2Print()
                Image2Print.calculate_printimage(path_in, path_out, dpix, dpiy, dimx, dimy, offsetx, offsety, rot, shrink, bg, sizex, sizey)
                ExecuteCalculatePrintimage = False

            if (ExecuteGetImageProperties == True):
                Image2Print = ImageProcessing.Image2Print()
                Image2Print.get_image_prop(path, dpimax)
                ExecuteGetImageProperties = False


    except IOError:
        pass
    finally:
        server.stop()
