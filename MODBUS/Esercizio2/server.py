from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_async_server():
    nreg = 200
    # Inizializzazione del datastore
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [15]*nreg),
        co=ModbusSequentialDataBlock(0, [16]*nreg),
        hr=ModbusSequentialDataBlock(0, [17]*nreg),
        ir=ModbusSequentialDataBlock(0, [18]*nreg))
    context = ModbusServerContext(slaves=store, single=True)

    # Inizializzazione delle informazioni del Server
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'TestLab-IoT'
    identity.ProductCode = 'TestLab-IoT'
    identity.VendorUrl = ''
    identity.ProductName = 'Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = '3.0.2'

    # Start TCP Server
    StartTcpServer(context=context, host='localhost',\
                   identity=identity, address=("127.0.0.1", 502))

if __name__ == "__main__":
    print('Modbus server started on localhost port 502')
    run_async_server()