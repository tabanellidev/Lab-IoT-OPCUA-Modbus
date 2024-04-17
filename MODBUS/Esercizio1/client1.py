from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50001)

# Coordinate di lettura / scrittura
reg=10

# Identificativo del dispositivo modbus (server)
address=0

# Dati da inviare
data = [31,32,33,34,3]

# Scrittura dei dati sui registri (40001 to 40005)
print('Write',data)
builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)

# Building del payload in formato 16bit
for d in data:
    builder.add_16bit_int(int(d))
payload = builder.build()

# Scrittura dei dati sul holdings register
result  = client.write_registers(int(reg), payload, skip_encode=True, unit=int(address))

# Chiusura connessione
client.close()