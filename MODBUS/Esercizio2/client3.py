from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50002)

# Coordinate di lettura / scrittura dei due registri 
reg_1 = 50
reg_2 = 100

# Identificativo del dispositivo modbus (server)
address=0

# Dati da leggere
numero_dati_da_leggere_reg1 = 5
numero_dati_da_leggere_reg2 = 1

# Lettura dei registri per confrontare i dati iniziali e finali
rd_1 = client.read_holding_registers(reg_1, numero_dati_da_leggere_reg1).registers
rd_2 = client.read_holding_registers(reg_2, numero_dati_da_leggere_reg2).registers
print('Read first registry', rd_1)
print('Read second registry', rd_2)

# Chiusura del client
client.close()