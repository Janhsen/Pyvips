
import sys
from opcua import Client
from opcua import ua
import logging
sys.path.insert(0, "..")
logging.basicConfig()

if __name__ == "__main__":
    
    client = Client("opc.tcp://localhost:4840")
    
    try:
        client.connect()

        # Get UA nodes in root
        root = client.get_root_node()

        # get a specific variable node knowing its node id
        var = client.get_node("ns=4;s=|var|ODESYS Control RTE x64 .Application.Main.PLC.ImageProcessing.stCalculatePrintImage.stIn.nDpiX")
        print("Value read from int16 variable: %s" % var.get_value())
        logging.info("Value read from int16 variable")

    finally:
        client.disconnect()
