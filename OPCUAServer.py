import sys
import time
import ImageProcessing
from opcua import ua, Server
sys.path.insert(0, "..")

if __name__ == "__main__":

    # setup server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/fraunhoferipa/server/")
    server.set_server_name("Fraunhofer OpcUa Server")
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
    uri = "http://ipa.fraunhofer.de"
    idx = server.register_namespace(uri)
    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()
    # populating our address space
    OPCUA_ImageProcessing = objects.add_object(idx, "stImageProcessing")
    CalculatePrintimage = OPCUA_ImageProcessing.add_object(idx, "stCalculatePrintimage")
    CalculatePrintimageIn = CalculatePrintimage.add_object(idx, "stIn")
    CalculatePrintimageOut = CalculatePrintimage.add_object(idx, "stOut")
    GetImageProperties = OPCUA_ImageProcessing.add_object(idx, "stGetImageProperties")

    ExecuteCalculatePrintimage = CalculatePrintimage.add_variable(idx, "xExecute", False) 
    ExecuteCalculatePrintimage.set_writable()
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
    shrink = CalculatePrintimageIn.add_variable(idx, "xShrink", False)
    shrink.set_writable()
    bg = CalculatePrintimageIn.add_variable(idx, "arrBG", [255, 255, 255])
    bg.set_writable()
    sizex = CalculatePrintimageIn.add_variable(idx, "rSizeX", .1)
    sizex.set_writable()
    sizey = CalculatePrintimageIn.add_variable(idx, "rSizeX", .1)
    sizey.set_writable()

    ExecuteGetImageProperties = GetImageProperties.add_variable(idx, "xExecute", False)
    ExecuteGetImageProperties.set_writable()

    GetImagePropertiesIn = GetImageProperties.add_object(idx, "stIn")
    path = GetImagePropertiesIn.add_variable(idx, "path", "./data/Test.tiff")
    path.set_writable()
    dpimax = GetImagePropertiesIn.add_variable(idx, "dpimax", 100)
    dpimax.set_writable()
    GetImagePropertiesOut = GetImageProperties.add_object(idx, "stOut")
    width_px = GetImagePropertiesOut.add_variable(idx, "nWidth_px", 0)
    height_px = GetImagePropertiesOut.add_variable(idx, "nHeight_px", 0)
    dpmmx = GetImagePropertiesOut.add_variable(idx, "rDpmmx", 0.0)
    dpmmy = GetImagePropertiesOut.add_variable(idx, "rDpmmy", 0.0)
    width_mm = GetImagePropertiesOut.add_variable(idx, "rWidth_mm", 0.0)
    height_mm = GetImagePropertiesOut.add_variable(idx, "rHeight_mm", 0.0)
    DPIx = GetImagePropertiesOut.add_variable(idx, "nDPIx", 0)
    DPIy = GetImagePropertiesOut.add_variable(idx, "nDPIy", 0)

    # starting!
    server.start()

    try:
        while True:
            time.sleep(0.05)  
            if (ExecuteCalculatePrintimage.get_value() is True):
                Image2Print = ImageProcessing.Image2Print()
                print(path_in.get_value())
                Image2Print.calculate_printimage(dpix = dpix.get_value(), 
                                                 dpiy = dpiy.get_value(), 
                                                 dimx = dimx.get_value(), 
                                                 dimy = dimy.get_value(), 
                                                 path_in = path_in.get_value(),
                                                 path_out = path_out.get_value(),
                                                 sizex = sizex.get_value(), 
                                                 sizey = sizey.get_value(),
                                                 rot = rot.get_value(), 
                                                 offsetx = offsetx.get_value(), 
                                                 offsety = offsety.get_value(), 
                                                 shrink = shrink.get_value(), 
                                                 bg = bg.get_value())
                ExecuteCalculatePrintimage.set_value(False)

            if (ExecuteGetImageProperties.get_value() is True):
                Image2Print = ImageProcessing.Image2Print()
                img_prop = Image2Print.get_image_prop(path=path.get_value(),
                                                        dpimax=dpimax.get_value())            
                width_px.set_value(img_prop['width_px'])
                height_px.set_value(img_prop['height_px'])
                dpmmx.set_value(img_prop['dpmmx'])
                dpmmy.set_value(img_prop['dpmmy'])
                width_mm.set_value(img_prop['width_mm'])
                height_mm.set_value(img_prop['height_mm'])
                DPIx.set_value(img_prop['DPIx'])
                DPIy.set_value(img_prop['DPIy'])
                ExecuteGetImageProperties.set_value(False)

    except IOError:
        pass
    finally:
        server.stop()
