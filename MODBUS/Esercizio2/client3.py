from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

#Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50002)
#Coordinate di lettura / scrittura
reg_1 = 50
reg_2 = 100
address=0

#Dati da leggere
data_1 = [0, 0, 0, 0, 0]
data_2 = [0.0]

#Lettura dei registri
rd_1 = client.read_holding_registers(reg_1,len(data_1)).registers
rd_2 = client.read_holding_registers(reg_2,len(data_2)).registers
print('Read first registry',rd_1)
print('Read second registry',rd_2)

client.close()