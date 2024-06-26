import time
from opcua import ua, Server, uamethod

check = True

def move():
    global check
    check = True

# Metodo per fermare la macchina, settando il flag check a False
def stop():
    global check
    check = False

# Metodo per controllare la macchina
@uamethod
def controls(parent, x):    
    
    msg = "Comando invalido"

    if x == "Stop":
        stop()              # chiamo la funzione stop
        msg = "Fermato"     # setto il messaggio di ritorno

    if x == "Start":
        move()
        msg = "Ripartito"

    return msg

if __name__ == "__main__":

    #Server setup
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")

    #Namespace Setup
    uri = "OPCUA_SERVER"
    idx = server.register_namespace(uri)

    #Objects Node
    objects = server.get_objects_node()

    #Aggiunta di oggetti e variabili all'Objects node
    macchinaL1 = objects.add_object(idx, "Linea1")
    varmL1 = macchinaL1.add_variable(idx, "varL1", 0)
    #Impostare la variabile come modificabile dal client
    varmL1.set_writable()    

    #Print degli ids
    print('-------------------------')
    print("Object node is ", objects)
    print("Linea1 ", macchinaL1)
    print("varL1  ", varmL1)
    print('-------------------------')
    
    # Definizione degli argomenti di Input/Output
    inarg= ua.Argument()
    inarg.Name= "Input"                                 # Nome dell'argomento
    inarg.DataType= ua.NodeId(ua.ObjectIds.String)      # Tipo di dato dell'argomento
    inarg.ValueRank= -1
    inarg.ArrayDimensions= []
    inarg.Description= ua.LocalizedText("Comando")      # Descrizione dell'argomento

    outarg= ua.Argument()
    outarg.Name= "Output"
    outarg.DataType= ua.NodeId(ua.ObjectIds.String)
    outarg.ValueRank= -1
    outarg.ArrayDimensions= []
    outarg.Description= ua.LocalizedText("Messaggio")

    # Istanzio l’oggetto metodo controls
    multiply_node = objects.add_method(idx, "controls", controls, [inarg], [outarg]) # Creo il metodo controls passando gli argomenti in input (inarg) e in output (outarg)
                                                                                     # idx è il namespace 

    server.start()

    try:
        while True:
            while check:
                time.sleep(1)
                #Recupero del valore della variabile
                tempL1 = varmL1.get_value()
                
                tempL1 += 1

                #Scrittura del valore della variabile
                varmL1.set_value(tempL1)

                print("Valore L1: ", tempL1)
            

    finally:
        server.stop()