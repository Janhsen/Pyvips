
import sys
from opcua import Client
from opcua import ua
import logging
from threading import *  # function which accepts an array of numbers and prints their sum
sys.path.insert(0, "..")
logging.basicConfig()

#Node Defs
stCalculatePrintImage = {'xExecute': 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.xExecute',
                        'stIn': {   'arrBg'     : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.arrBg',
                                    'nDpiX'     : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiX',
                                    'nDpiY'     : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiY',
                                    'rDimX'     : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rDimX',
                                    'rDimY'     : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rDimY',
                                    'rOffsetX'  : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rOffsetX',
                                    'rOffsetY'  : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rOffsetY',
                                    'rRot'      : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rRot',
                                    'rSizeX'    : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rSizeX',
                                    'rSizeY'    : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rSizeY',
                                    'sPathIn'   : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.sPathIn',
                                    'sPathOut'  : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.sPathOut',
                                    'xShrink'   : 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.xShrink'
                                }
                        }
stGetImageProperties = {'xExecute': 'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stGetImageProperties.xExecute'}


if __name__ == "__main__":
    
    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()
        # get a specific variable node knowing its node id
        var = client.get_node(stCalculatePrintImage.get('xExecute'))
        print("Value read from variable stCalculatePrintImage.xExecute : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('arrBg'))
        print("Value read from variable stCalculatePrintImage.stIn.arrBg : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('nDpiX'))
        print("Value read from variable stCalculatePrintImage.stIn.nDpiX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('nDpiY'))
        print("Value read from variable stCalculatePrintImage.stIn.nDpiY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rDimX'))
        print("Value read from variable stCalculatePrintImage.stIn.rDimX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rDimY'))
        print("Value read from variable stCalculatePrintImage.stIn.rDimY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rOffsetX'))
        print("Value read from variable stCalculatePrintImage.stIn.rOffsetX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rOffsetY'))
        print("Value read from variable stCalculatePrintImage.stIn.rOffsetY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rRot'))
        print("Value read from variable stCalculatePrintImage.stIn.rRot : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rSizeX'))
        print("Value read from variable stCalculatePrintImage.stIn.rSizeX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rSizeY'))
        print("Value read from variable stCalculatePrintImage.stIn.rSizeY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('sPathIn'))
        print("Value read from variable stCalculatePrintImage.stIn.sPathIn : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('sPathOut'))
        print("Value read from variable stCalculatePrintImage.stIn.sPathOut : %s" % var.get_value())
    finally:
        client.disconnect()