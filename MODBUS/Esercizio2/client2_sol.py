from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

#Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)

#[2.1] - Definire i registri di lettura e scrittura
reg_1=50

reg_2 = 100
address=0

#Dati da leggere
data = [0,0,0,0,0]

#[2.2] - Lettura dai registri
rd = client.read_holding_registers(reg_1,len(data)).registers
print('Read',rd)

#[2.3] - Calcolo della media
mean = 0
for n in rd:
    mean = mean + n

mean = mean / len(rd)
print(mean)


#[2.4] - Scrittura sul registro
print('Write',mean)
builder = BinaryPayloadBuilder(byteorder=Endian.Big,\
                                wordorder=Endian.Little)

#Building del payload e scrittura sui registri
builder.add_16bit_int(int(mean))

payload = builder.build()
result  = client.write_registers(int(reg_2), payload,\
            skip_encode=True, unit=int(address))


client.close()