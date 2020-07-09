import sys
sys.path.insert(0, "..")
import time

import ImageProcessing

from opcua import ua, Server, uamethod


#execute Python script for ImageProcessing

@uamethod
def printImage(     IMAGEPATH_EXISTING,
                    IMAGEPATH_EXISTING_SVG_1,
                    IMAGEPATH_EXISTING_SVG_2,
                    IMAGEPATH_SYNTAX,
                    IMAGEPATH_WRONGENDING,
                    IMAGEPATH_NOTEXISTING,
                    IMAGEPATH_SAVE,
                    DPIX_1,
                    DPIY_1,
                    DPIX_2,
                    DPIY_2,
                    DPIX_3,
                    DPIY_3,
                    DIMX,
                    DIMY,
                    OFFSETX,
                    OFFSETY,
                    ROT,
                    SHRINK,
                    BG,
                    SIZEX,
                    SIZEY):
    
    Image2Print = ImageProcessing.Image2Print()     #initialise class
    Image2Print.calculate_printimage(               #execute function
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
    return True
        

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/fraunhoferipa/server/")#freeopcua
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "TestVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    IMAGEPATH_EXISTING = myobj.add_variable(idx, "IMAGEPATH_EXISTING", "./data/Test.tiff")
    IMAGEPATH_EXISTING.set_writable()
    IMAGEPATH_EXISTING_SVG_1 = myobj.add_variable(idx, "IMAGEPATH_EXISTING_SVG_1", "./data/test_corel.svg")
    IMAGEPATH_EXISTING_SVG_1.set_writable()
    IMAGEPATH_EXISTING_SVG_2 = myobj.add_variable(idx, "IMAGEPATH_EXISTING_SVG_2", "./data/test_inkscape.svg")
    IMAGEPATH_EXISTING_SVG_2.set_writable()
    IMAGEPATH_SYNTAX = myobj.add_variable(idx, "IMAGEPATH_SYNTAX", "./data/Test.TIFF")
    IMAGEPATH_SYNTAX.set_writable()
    IMAGEPATH_WRONGENDING = myobj.add_variable(idx, "IMAGEPATH_WRONGENDING","./data/x.jpg")
    IMAGEPATH_WRONGENDING.set_writable()
    IMAGEPATH_NOTEXISTING = myobj.add_variable(idx, "IMAGEPATH_NOTEXISTING", "./data/Tester.jpg")
    IMAGEPATH_NOTEXISTING.set_writable()
    IMAGEPATH_SAVE = myobj.add_variable(idx, "IMAGEPATH_SAVE", "./data/result.tiff")
    IMAGEPATH_SAVE.set_writable()
    DPIX_1 = myobj.add_variable(idx,"DPIX_1", 100)
    DPIX_1.set_writable()
    DPIY_1 = myobj.add_variable(idx, "DPIY_1", 200)
    DPIY_1.set_writable()
    DPIX_2 = myobj.add_variable(idx, "DPIX_2", 100)
    DPIX_2.set_writable()
    DPIY_2 = myobj.add_variable(idx, "DPIY_2", 100)
    DPIY_2.set_writable()
    DPIX_3 = myobj.add_variable(idx, "DPIX_3", 300)
    DPIX_3.set_writable()
    DPIY_3 = myobj.add_variable(idx, "DPIY_3", 100)
    DPIY_3.set_writable()
    DIMX = myobj.add_variable(idx, "DIMX", 125.4)
    DIMX.set_writable()
    DIMY = myobj.add_variable(idx, "DIMY", 150.8)
    DIMY.set_writable()
    OFFSETX = myobj.add_variable(idx, "OFFSETX", 0)
    OFFSETX.set_writable()
    OFFSETY = myobj.add_variable(idx, "OFFSETY", 0)
    OFFSETY.set_writable()
    ROT = myobj.add_variable(idx, "ROT", 0)
    ROT.set_writable()
    SHRINK = myobj.add_variable(idx, "SHRINK", True)
    SHRINK.set_writable()
    BG =  myobj.add_variable(idx, "BG", [240, 240, 240])
    BG.set_writable()
    SIZEX = myobj.add_variable(idx, "SIZEX", 1)
    SIZEX.set_writable()
    SIZEY = myobj.add_variable(idx, "SIZEY", 1)
    SIZEY.set_writable()

    execPrintImage =  myobj.add_method(idx, "Calulate_printImage", printImage, [IMAGEPATH_EXISTING,IMAGEPATH_EXISTING_SVG_1,IMAGEPATH_EXISTING_SVG_2,IMAGEPATH_SYNTAX,IMAGEPATH_WRONGENDING,IMAGEPATH_NOTEXISTING,IMAGEPATH_SAVE,DPIX_1,DPIY_1,DPIX_2,DPIY_2,DPIX_3,DPIY_3,DIMX,DIMY,OFFSETX,OFFSETY,ROT,SHRINK,BG,SIZEX,SIZEY], [ua.VariantType.Boolean])
    

    # starting!
    server.start()
    
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()