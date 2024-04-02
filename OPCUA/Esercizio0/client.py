from opcua import Client

if __name__ == "__main__":
    url_server = "opc.tcp://localhost:4840"
    #Client setup
    client = Client(url_server)
    try:
        client.connect()

        #Recupero del nodo root
        root = client.get_root_node()
        print("Root node is: ", root)

        
        print("Children of root are: ", root.get_children()) # Recupero dei figli del nodo root, ovvero Objects, Types e Views

        #Un oggetto si può recuperare specificando il suo nome oppure il suo identificativo
        objects = root.get_child(["0:Objects"]) #Recupero dell'oggetto Objects
                                                # 0: indica il namespace
        
        print("Children of Objects are ", objects.get_children()) # Recupero dei figli dell'oggetto Objects
                                                                  # I figlio sono Server e Linea1


        # Recupero degli elementi tramite la navigazione dell'Address Space
        # E li memorizzo in variabili
        macchinaL1 = root.get_child(["0:Objects", "2:Linea1"])          # Recupero dell'oggetto Linea1 di Objects 
                                                                        # Linea1 si trova nel nemaspace 2
        varmL1 = root.get_child(["0:Objects", "2:Linea1", "2:varL1"])   # Recupero della variabile varL1 di Linea1 di Objects
                                                                        # varL1 si trova nel namespace 2 (stesso nemaspace di Linea1)
        #Print degli Ids di Linea1 e varL1
        print("Linea1: ", macchinaL1)
        print("varL1:  ", varmL1)
        
        #Print del valore della variabile
        print(varmL1.get_value())


    finally:
        # Disconessione del client
        client.disconnect()