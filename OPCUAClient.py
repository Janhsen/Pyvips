
import sys
from opcua import Client
from opcua import ua
import logging
from threading import *  # function which accepts an array of numbers and prints their sum
sys.path.insert(0, "..")
logging.basicConfig()

#Helper
def dict_depth(dic, level = 1): 
      
    if not isinstance(dic, dict) or not dic: 
        return level 
    return max(dict_depth(dic[key], level + 1) 
                               for key in dic) 

#Node Defs
stCalculatePrintImage = {'xExecute': {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.xExecute'},
                        'stIn': {   'arrBg'     : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.arrBg'},
                                    'nDpiX'     : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiX'},
                                    'nDpiY'     : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiY'},
                                    'rDimX'     : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rDimX'},
                                    'rDimY'     : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rDimY'},
                                    'rOffsetX'  : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rOffsetX'},
                                    'rOffsetY'  : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rOffsetY'},
                                    'rRot'      : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rRot'},
                                    'rSizeX'    : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rSizeX'},
                                    'rSizeY'    : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rSizeY'},
                                    'sPathIn'   : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.sPathIn'},
                                    'sPathOut'  : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.sPathOut'},
                                    'xShrink'   : {'NodeID':'ns=4;s=|var|CODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.xShrink'}
                                }
                        }


if __name__ == "__main__":
    
    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()

        # get a specific variable node knowing its node id
        stCalculatePrintImage['stIn']['arrBg']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('arrBg').get('NodeID'))
        stCalculatePrintImage['stIn']['arrBg']['value'] = stCalculatePrintImage.get('stIn').get('arrBg').get('node').get_value()
      
        var = client.get_node(stCalculatePrintImage.get('stIn').get('arrBg').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.arrBg : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('nDpiX').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.nDpiX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('nDpiY').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.nDpiY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rDimX').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rDimX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rDimY').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rDimY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rOffsetX').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rOffsetX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rOffsetY').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rOffsetY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rRot').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rRot : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rSizeX').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rSizeX : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('rSizeY').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.rSizeY : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('sPathIn').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.sPathIn : %s" % var.get_value())
        var = client.get_node(stCalculatePrintImage.get('stIn').get('sPathOut').get('NodeID'))
        print("Value read from variable stCalculatePrintImage.stIn.sPathOut : %s" % var.get_value())
    finally:
        client.disconnect()