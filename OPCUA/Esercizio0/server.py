import time
from opcua import ua, Server


if __name__ == "__main__":

    # Server setup
    # Specificando l'indirizzo del server e la porta in ascolto
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")

    # Namespace Setup
    uri = "OPCUA_SERVER" # Definizone del namespace
    idx = server.register_namespace(uri) # Si registra il server con il namespace specificato

    # Objects Node
    objects = server.get_objects_node()

    # Fase 1 - Associazione 
    # Creazione di un oggetto e di una variabile all'interno dell'Objects node

    # Aggiunta di oggetti e variabili all'Objects node
    macchinaL1 = objects.add_object(idx, "Linea1")      # Inizializzazione dell'oggetto Linea1 specificando namespace e nome
    varmL1 = macchinaL1.add_variable(idx, "varL1", 0)   # Inizializzazione della variabile varL1 specificando namespace, nome e valore iniziale (0)
    
    # Impostare la variabile come modificabile dal client
    varmL1.set_writable()    

    # Fase 2 - Lavorazione
    # Si simula la lavorazione della macchina, incrementando la variabile di 1 ad ogni ciclo
    # Print degli ids
    print('-------------------------')
    print("Object node is ", objects)
    print("Linea1 ", macchinaL1)
    print("varL1  ", varmL1)
    print('-------------------------')
    

    server.start()

    try:
        # Ciclo for per incrementare il valore della variabile + 1 ad ogni ciclo e stamparlo
        while True:
            #Recupero del valore della variabile
            tempL1 = varmL1.get_value()
            
            tempL1 += 1

            #Scrittura del valore della variabile
            varmL1.set_value(tempL1)

            print("Valore L1: ", tempL1)
            
            # sleep per rallentare il ciclo
            time.sleep(1)
            

    finally:
        server.stop()