from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50000)

# Coordinate di lettura / scrittura
reg=0

# Identificativo del dispositivo modbus (server)
address=0

# Dati da inviare
data = [1,2,3,4,5]

# Scrittura dei dati sui registri
print('Write', data)

# Realizzazione del costruttore del builder
builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)

# Building del payload in formato 16bit
for d in data:
    builder.add_16bit_int(int(d))
payload = builder.build()

# Scrittura dei dati sul holdings register
# skip_encode=True serve per non codificare i dati in quanto sono stati già correttamente codificati attraverso il builder
result  = client.write_registers(int(reg), payload, skip_encode=True, unit=int(address))

# Lettura dei registri
numero_dati_da_leggere = 5
rd = client.read_holding_registers(reg, numero_dati_da_leggere).registers
print('Read', rd)

# Chiusura del client
client.close()