import sys
from opcua import Client
from opcua import ua
import threading
import time
import ImageProcessing
sys.path.insert(0, "..")

#Node Defs
xHeartbeat = {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.xHeartbeat'}

stCalculatePrintImage = {'xExecute': {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.xExecute'},
                        'stIn': {   'arrBg'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.arrBg'},
                                    'nDpiX'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiX'},
                                    'nDpiY'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiY'},
                                    'rDimX'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rDimX'},
                                    'rDimY'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rDimY'},
                                    'rOffsetX'  : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rOffsetX'},
                                    'rOffsetY'  : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rOffsetY'},
                                    'rRot'      : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rRot'},
                                    'rSizeX'    : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rSizeX'},
                                    'rSizeY'    : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.rSizeY'},
                                    'sPathIn'   : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.sPathIn'},
                                    'sPathOut'  : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.sPathOut'},
                                    'xShrink'   : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.xShrink'}
                                },
                        'stOut': {  'xError'    : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stOut.xError'}}                                   
                        }

stGetImageProperties = {'xExecute': {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.xExecute'},
                        'stIn': {   'nDpiMax'       : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stIn.nDpiMax'},
                                    'strPath'       : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stIn.strPath'}
                                },
                        'stOut': {  'nWidth_px'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.nWidth_px'},
                                    'nHeigth_px'    : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.nHeight_px'},
                                    'rWidth_mm'     : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.rWidth_mm'},
                                    'rHeigth_mm'    : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.rHeight_mm'},
                                    'rDpmmX'        : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.rDpmmX'},
                                    'rDpmmY'        : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.rDpmmY'},
                                    'nDpiX'         : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.nDpiX'},
                                    'nDpiY'         : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.nDpiY'},
                                    'xError'        : {'NodeID':'ns=4;s=|var|CODESYS Control Win V3.Application.Main.PLC.ImageProcessing.stGetImageProperties.stOut.xError'}
                                }
                        }


def Heartbeat():
    while True:
        xHeartbeat.get('node').set_value(not(xHeartbeat.get('node').get_value()))
        time.sleep(1)
        #print('xHeartbeat :', xHeartbeat.get('node').get_value())
       

if __name__ == "__main__":


    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()

        ### Register / Get Nodes
        print('Get nodes')
        xHeartbeat['node'] = client.get_node(xHeartbeat.get('NodeID'))
        stCalculatePrintImage['xExecute']['node'] = client.get_node(stCalculatePrintImage.get('xExecute').get('NodeID'))
        stCalculatePrintImage['stIn']['arrBg']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('arrBg').get('NodeID'))
        stCalculatePrintImage['stIn']['nDpiX']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('nDpiX').get('NodeID'))
        stCalculatePrintImage['stIn']['nDpiY']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('nDpiY').get('NodeID'))
        stCalculatePrintImage['stIn']['rDimX']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rDimX').get('NodeID'))
        stCalculatePrintImage['stIn']['rDimY']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rDimY').get('NodeID'))
        stCalculatePrintImage['stIn']['rOffsetX']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rOffsetX').get('NodeID'))
        stCalculatePrintImage['stIn']['rOffsetY']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rOffsetY').get('NodeID'))
        stCalculatePrintImage['stIn']['rRot']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rRot').get('NodeID'))
        stCalculatePrintImage['stIn']['rSizeX']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rSizeX').get('NodeID'))
        stCalculatePrintImage['stIn']['rSizeY']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('rSizeY').get('NodeID'))
        stCalculatePrintImage['stIn']['sPathIn']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('sPathIn').get('NodeID'))
        stCalculatePrintImage['stIn']['sPathOut']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('sPathOut').get('NodeID'))
        stCalculatePrintImage['stIn']['xShrink']['node'] = client.get_node(stCalculatePrintImage.get('stIn').get('xShrink').get('NodeID'))
        stCalculatePrintImage['stOut']['xError']['node'] = client.get_node(stCalculatePrintImage.get('stOut').get('xError').get('NodeID'))

        stGetImageProperties['xExecute']['node'] = client.get_node(stGetImageProperties.get('xExecute').get('NodeID'))
        stGetImageProperties['stIn']['nDpiMax']['node'] = client.get_node(stGetImageProperties.get('stIn').get('nDpiMax').get('NodeID'))
        stGetImageProperties['stIn']['strPath']['node'] = client.get_node(stGetImageProperties.get('stIn').get('strPath').get('NodeID'))
        stGetImageProperties['stOut']['nWidth_px']['node'] = client.get_node(stGetImageProperties.get('stOut').get('nWidth_px').get('NodeID'))
        stGetImageProperties['stOut']['nHeigth_px']['node'] = client.get_node(stGetImageProperties.get('stOut').get('nHeigth_px').get('NodeID'))
        stGetImageProperties['stOut']['rWidth_mm']['node'] = client.get_node(stGetImageProperties.get('stOut').get('rWidth_mm').get('NodeID'))
        stGetImageProperties['stOut']['rHeigth_mm']['node'] = client.get_node(stGetImageProperties.get('stOut').get('rHeigth_mm').get('NodeID'))        
        stGetImageProperties['stOut']['rDpmmX']['node'] = client.get_node(stGetImageProperties.get('stOut').get('rDpmmX').get('NodeID'))
        stGetImageProperties['stOut']['rDpmmY']['node'] = client.get_node(stGetImageProperties.get('stOut').get('rDpmmY').get('NodeID'))  
        stGetImageProperties['stOut']['nDpiX']['node'] = client.get_node(stGetImageProperties.get('stOut').get('nDpiX').get('NodeID'))
        stGetImageProperties['stOut']['nDpiY']['node'] = client.get_node(stGetImageProperties.get('stOut').get('nDpiY').get('NodeID'))  
        stGetImageProperties['stOut']['xError']['node'] = client.get_node(stGetImageProperties.get('stOut').get('xError').get('NodeID'))

        # Start xHeartbeat Thread 
        t = threading.Thread(target=Heartbeat)  
        t.start()
##
        #Get get Node values
        #print('Get node values')
        #xHeartbeat['value'] = xHeartbeat.get('node').get_value()
        #stCalculatePrintImage['xExecute']['value'] = stCalculatePrintImage.get('xExecute').get('node').get_value()
        #stCalculatePrintImage['stIn']['arrBg']['value'] = stCalculatePrintImage.get('stIn').get('arrBg').get('node').get_value()
        #stCalculatePrintImage['stIn']['nDpiX']['value'] = stCalculatePrintImage.get('stIn').get('nDpiX').get('node').get_value()
        #stCalculatePrintImage['stIn']['nDpiY']['value'] = stCalculatePrintImage.get('stIn').get('nDpiY').get('node').get_value()
        #stCalculatePrintImage['stIn']['rDimX']['value'] = stCalculatePrintImage.get('stIn').get('rDimX').get('node').get_value()
        #stCalculatePrintImage['stIn']['rDimY']['value'] = stCalculatePrintImage.get('stIn').get('rDimY').get('node').get_value()
        #stCalculatePrintImage['stIn']['rOffsetX']['value'] = stCalculatePrintImage.get('stIn').get('rOffsetX').get('node').get_value()
        #stCalculatePrintImage['stIn']['rOffsetY']['value'] = stCalculatePrintImage.get('stIn').get('rOffsetY').get('node').get_value()
        #stCalculatePrintImage['stIn']['rRot']['value'] = stCalculatePrintImage.get('stIn').get('rRot').get('node').get_value()
        #stCalculatePrintImage['stIn']['rSizeX']['value'] = stCalculatePrintImage.get('stIn').get('rSizeX').get('node').get_value()
        #stCalculatePrintImage['stIn']['rSizeY']['value'] = stCalculatePrintImage.get('stIn').get('rSizeY').get('node').get_value()
        #stCalculatePrintImage['stIn']['sPathIn']['value'] = stCalculatePrintImage.get('stIn').get('sPathIn').get('node').get_value()
        #stCalculatePrintImage['stIn']['sPathOut']['value'] = stCalculatePrintImage.get('stIn').get('sPathOut').get('node').get_value()
        #stCalculatePrintImage['stIn']['xShrink']['value'] = stCalculatePrintImage.get('stIn').get('xShrink').get('node').get_value()
        #stCalculatePrintImage['stOut']['xError']['value'] = stCalculatePrintImage.get('stOut').get('xError').get('node').get_value()

        #stGetImageProperties['xExecute']['value'] = stGetImageProperties.get('xExecute').get('node').get_value()
        #stGetImageProperties['stIn']['nDpiMax']['value'] = stGetImageProperties.get('stIn').get('nDpiMax').get('node').get_value()
        #stGetImageProperties['stIn']['strPath']['value'] = stGetImageProperties.get('stIn').get('strPath').get('node').get_value()
        #stGetImageProperties['stOut']['nWidth_px']['value'] = stGetImageProperties.get('stOut').get('nWidth_px').get('node').get_value()
        #stGetImageProperties['stOut']['nHeigth_px']['value'] = stGetImageProperties.get('stOut').get('nHeigth_px').get('node').get_value()
        #stGetImageProperties['stOut']['rWidth_mm']['value'] = stGetImageProperties.get('stOut').get('rWidth_mm').get('node').get_value()
        #stGetImageProperties['stOut']['rHeigth_mm']['value'] = stGetImageProperties.get('stOut').get('rHeigth_mm').get('node').get_value()
        #stGetImageProperties['stOut']['rDpmmX']['value'] = stGetImageProperties.get('stOut').get('rDpmmX').get('node').get_value()
        #stGetImageProperties['stOut']['rDpmmY']['value'] = stGetImageProperties.get('stOut').get('rDpmmY').get('node').get_value()
        #stGetImageProperties['stOut']['nDpiX']['value'] = stGetImageProperties.get('stOut').get('nDpiX').get('node').get_value()
        #stGetImageProperties['stOut']['nDpiY']['value'] = stGetImageProperties.get('stOut').get('nDpiY').get('node').get_value()
        #stGetImageProperties['stOut']['xError']['value'] = stGetImageProperties.get('stOut').get('xError').get('node').get_value()

        ####  Read stCalculatePrintImage
        #print("\nValue read from variable xHeartbeat : %s" % xHeartbeat['value'])
        #print("\nValue read from variable stCalculatePrintImage.xExecute : %s" % stCalculatePrintImage['xExecute']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.arrBg : %s" % stCalculatePrintImage['stIn']['arrBg']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.nDpiX : %s" % stCalculatePrintImage['stIn']['nDpiX']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.nDpiY : %s" % stCalculatePrintImage['stIn']['nDpiY']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rDimX : %s" % stCalculatePrintImage['stIn']['rDimX']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rDimY : %s" % stCalculatePrintImage['stIn']['rDimY']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rOffsetX : %s" % stCalculatePrintImage['stIn']['rOffsetX']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rOffsetY : %s" % stCalculatePrintImage['stIn']['rOffsetY']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rRot : %s" % stCalculatePrintImage['stIn']['rRot']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rSizeX : %s" % stCalculatePrintImage['stIn']['rSizeX']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.rSizeY : %s" % stCalculatePrintImage['stIn']['rSizeY']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.sPathIn : %s" % stCalculatePrintImage['stIn']['sPathIn']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.sPathOut : %s" % stCalculatePrintImage['stIn']['sPathOut']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.xShrink : %s" % stCalculatePrintImage['stIn']['xShrink']['value'])
        #print("Value read from variable stCalculatePrintImage.stIn.xError : %s" % stCalculatePrintImage['stOut']['xError']['value'])

        #print("\nValue read from variable stGetImageProperties.xExecute : %s" % stGetImageProperties['xExecute']['value'])
        #print("Value read from variable stGetImageProperties.stIn.nDpiMax : %s" % stGetImageProperties['stIn']['nDpiMax']['value'])
        #print("Value read from variable stGetImageProperties.stIn.strPath : %s" % stGetImageProperties['stIn']['strPath']['value'])
        #print("Value read from variable stGetImageProperties.stOut.nWidth_px : %s" % stGetImageProperties['stOut']['nWidth_px']['value'])
        #print("Value read from variable stGetImageProperties.stOut.nHeigth_px : %s" % stGetImageProperties['stOut']['nHeigth_px']['value'])
        #print("Value read from variable stGetImageProperties.stOut.rWidth_mm : %s" % stGetImageProperties['stOut']['rWidth_mm']['value'])
        #print("Value read from variable stGetImageProperties.stOut.rHeigth_mm : %s" % stGetImageProperties['stOut']['rHeigth_mm']['value'])
        #print("Value read from variable stGetImageProperties.stOut.rDpmmX : %s" % stGetImageProperties['stOut']['rDpmmX']['value'])
        #print("Value read from variable stGetImageProperties.stOut.rDpmmY : %s" % stGetImageProperties['stOut']['rDpmmY']['value'])
        #print("Value read from variable stGetImageProperties.stOut.nDpiX : %s" % stGetImageProperties['stOut']['nDpiX']['value'])
        #print("Value read from variable stGetImageProperties.stOut.nDpiY : %s" % stGetImageProperties['stOut']['nDpiY']['value'])
        #print("Value read from variable stGetImageProperties.stOut.xError : %s" % stGetImageProperties['stOut']['xError']['value'])
##
        ## Main Loop
        while True:
            time.sleep(0.1)  
            if (stCalculatePrintImage.get('xExecute').get('node').get_value() is True):
                Image2Print = ImageProcessing.Image2Print()
                calc_result = Image2Print.calculate_printimage(dpix = stCalculatePrintImage.get('stIn').get('nDpiX').get('node').get_value(), 
                                                 dpiy = stCalculatePrintImage.get('stIn').get('nDpiY').get('node').get_value(),
                                                 dimx = stCalculatePrintImage.get('stIn').get('rDimX').get('node').get_value(), 
                                                 dimy = stCalculatePrintImage.get('stIn').get('rDimY').get('node').get_value(), 
                                                 path_in = stCalculatePrintImage.get('stIn').get('sPathIn').get('node').get_value(),
                                                 path_out = stCalculatePrintImage.get('stIn').get('sPathOut').get('node').get_value(),
                                                 sizex = stCalculatePrintImage.get('stIn').get('rSizeX').get('node').get_value(), 
                                                 sizey = stCalculatePrintImage.get('stIn').get('rSizeY').get('node').get_value(),
                                                 rot = stCalculatePrintImage.get('stIn').get('rRot').get('node').get_value(), 
                                                 offsetx = stCalculatePrintImage.get('stIn').get('rOffsetX').get('node').get_value(), 
                                                 offsety = stCalculatePrintImage.get('stIn').get('rOffsetY').get('node').get_value(), 
                                                 shrink = stCalculatePrintImage.get('stIn').get('xShrink').get('node').get_value(), 
                                                 bg = stCalculatePrintImage.get('stIn').get('arrBg').get('node').get_value())
                #write results back to server
                stCalculatePrintImage.get('stOut').get('xError').get('node').set_value(calc_result.get('xError'))
                stCalculatePrintImage.get('xExecute').get('node').set_value(False)

            if (stGetImageProperties.get('xExecute').get('node').get_value() is True):
                #int class
                Image2Print = ImageProcessing.Image2Print()

                #class method
                img_prop = Image2Print.get_image_prop(path=stGetImageProperties.get('stIn').get('strPath').get('node').get_value(),
                                                        dpimax= stGetImageProperties.get('stIn').get('nDpiMax').get('node').get_value())       

                #write back to server                                                                                                     
                stGetImageProperties.get('stOut').get('nWidth_px').get('node').set_value(img_prop['width_px'], ua.VariantType.Int32)
                stGetImageProperties.get('stOut').get('nHeigth_px').get('node').set_value(img_prop['height_px'], ua.VariantType.Int32)
                stGetImageProperties.get('stOut').get('rDpmmX').get('node').set_value(img_prop['dpmmx'], ua.VariantType.Float)
                stGetImageProperties.get('stOut').get('rDpmmY').get('node').set_value(img_prop['dpmmy'], ua.VariantType.Float)
                stGetImageProperties.get('stOut').get('rWidth_mm').get('node').set_value(img_prop['width_mm'], ua.VariantType.Float)
                stGetImageProperties.get('stOut').get('rHeigth_mm').get('node').set_value(img_prop['height_mm'], ua.VariantType.Float)
                stGetImageProperties.get('stOut').get('nDpiX').get('node').set_value(img_prop['DPIx'], ua.VariantType.Int16)
                stGetImageProperties.get('stOut').get('nDpiY').get('node').set_value(img_prop['DPIy'], ua.VariantType.Int16)
                stGetImageProperties.get('stOut').get('xError').get('node').set_value(img_prop['xError'], ua.VariantType.Boolean)
                stGetImageProperties.get('xExecute').get('node').set_value(False)
    except:
         pass
    finally:
        client.disconnect()
