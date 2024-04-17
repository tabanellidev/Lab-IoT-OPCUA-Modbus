from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50001)

#[1.1] - Selezionare l'offset del registro da leggere 
# Coordinate di lettura / scrittura
# reg = 

# Identificativo del dispositivo modbus (server)
# address =


#[1.2] - Definire dati da leggere
# Numero dati da leggere
# numero_dati_da_leggere = 

#[1.3] - Leggere e stampare
# Leggere e stampare
# rd = 

client.close()