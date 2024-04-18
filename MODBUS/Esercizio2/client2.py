from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time, struct

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50002)

#[2.1] - Definire due registri di lettura e scrittura (stare attenti ai registri che non si sovrappongono)
# Indizio: reg_1 deve essere lo stesso del client 1
#reg_1 = 

#reg_2 = 

# Identificativo del dispositivo modbus (server)
address=0

# Formato dati da leggere
numero_dati_da_leggere = 5

#[2.2] - Lettura dai registri 

#[2.3] - Una funzione per il calcolo della media

#[2.4] - Scrittura sul registro compreso la creazione del builder e il building del payload
# Se si desidera gestire il floating point, utilizzare il pacchetto struct utile per la gestione dei dati e la formattazione corretta


client.close()