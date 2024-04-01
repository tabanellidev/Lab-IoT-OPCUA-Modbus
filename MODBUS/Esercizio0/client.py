from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

#Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)
#Coordinate di lettura / scrittura
reg=0; 
address=0

#Dati da inviare
data = [1,2,3,4,5]

# Scrittura dei dati sui registri (40001 to 40005)
print('Write',data)
builder = BinaryPayloadBuilder(byteorder=Endian.Big,\
                                wordorder=Endian.Little)

#Building del payload e scrittura sui registri
for d in data:
    builder.add_16bit_int(int(d))
payload = builder.build()
result  = client.write_registers(int(reg), payload,\
            skip_encode=True, unit=int(address))

#Lettura dei registri
rd = client.read_holding_registers(reg,len(data)).registers
print('Read',rd)

client.close()