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
        
        #[2.4] - Recupero dell'oggetto "Linea2" e della sua variabile "varL2"
        macchinaL2 = root.get_child(["0:Objects", "2:Linea2"])
        varmL2 = root.get_child(["0:Objects", "2:Linea2", "2:varL2"])

        #Print degli Ids
        print("Linea1: ", macchinaL1)
        print("varL1:  ", varmL1)
        #[Facoltativo] - Print degli id
        print("Linea2: ", macchinaL2)
        print("varL2:  ", varmL2)

        #Print del valore della variabile
        print("Valore L1: ", varmL1.get_value())

        #[2.5] - Print del valore della variabile
        print("Valore L2: ", varmL2.get_value())

    finally:
        client.disconnect()