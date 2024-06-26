from opcua import Client

if __name__ == "__main__":
    #Client setup
    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()

        #Recupero del nodo root
        root = client.get_root_node()
        print("Root node is: ", root)

        
        print("Children of root are: ", root.get_children())

        #Un oggetto si può recuperare specificando il suo nome oppure il suo identificativo
        objects = root.get_child(["0:Objects"])

        print("Children of Objects are ", objects.get_children())


        # Recupero degli elementi tramite la navigazione dell'Address Space
        macchinaL1 = root.get_child(["0:Objects", "2:Linea1"])
        varmL1 = root.get_child(["0:Objects", "2:Linea1", "2:varL1"])
        
        #Print degli Ids
        print("Linea1: ", macchinaL1)
        print("varL1: ", varmL1)
        
        #Print del valore della variabile
        print("Valore letto prima della scrittura", varmL1.get_value())

        #[1.1] - Imposta il valore della variabile lato client

        #[1.2] - Print del valore della variabile


    finally:
        client.disconnect()