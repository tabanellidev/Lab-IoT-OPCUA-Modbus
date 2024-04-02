from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

#Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)
#[2.1] - Definire i registri di lettura e scrittura
#reg_1 = 

#reg_2 = 

address=0

#Dati da inviare
data = [0,0,0,0,0]

#[2.2] - Lettura dai registri

#[2.3] - Calcolo della media

#[2.4] - Scrittura sul registro


client.close()