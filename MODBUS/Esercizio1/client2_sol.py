from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

#Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)
#Coordinate di lettura / scrittura

#[5.1] - Selezionare l'offset del registro da leggere 
reg = 10
address=0

#Dati da leggere
data = [0,0,0,0,0]

#[5.2] - Leggere e stampare
#Lettura dei registri
rd = client.read_holding_registers(reg,len(data)).registers
print('Read',rd)

client.close()