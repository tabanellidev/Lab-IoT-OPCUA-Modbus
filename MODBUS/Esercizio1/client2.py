from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

#Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)
#Coordinate di lettura / scrittura

#[1.1] - Selezionare l'offset del registro da leggere 
#reg = 


#[1.2] - Definire dati da leggere
#data = 

#Leggere e stampare

client.close()