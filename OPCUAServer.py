import sys
sys.path.insert(0, "..")
import time

import ImageProcessing

from opcua import ua, Server, uamethod


#execute Python script for ImageProcessing
@uamethod
def PythonScript(trigger = True):
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

    execPythonSkript = myobj.add_method(idx, "ImageTrigger", PythonScript, [], [ua.VariantType.Boolean]) #sollen Variablen via opc ua übergeben werden? -> müssen in [] eingetetragen werden

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