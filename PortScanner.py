import sys
import socket
import threading

#Ensures The Scan Will Take No More Than 20 Seconds
socket.setdefaulttimeout(20)

#The Scan Function Makes Connection Then Checks if The Port Is Open
def scan(ipAddress, portConnecting):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipAddress, portConnecting))
        print(f"PORT {portConnecting} IS OPEN!")
        s.close()
    except:
        print(f"PORT {portConnecting} IS CLOSED!")
        
#Collects user input
try:

    args = sys.argv

    IP = str(args[1])

    PORT_START = int(args[2])

    PORT_END = int(args[3])

    CURRENT_PORT = PORT_START

    if((len(IP.split(".")) == 4) + (PORT_START == int()) + (PORT_END == int())):
        #Here We Run Threw The Ports The User Has Entered
        while(CURRENT_PORT <= PORT_END):
            x = threading.Thread(target=scan, args = (IP, CURRENT_PORT))
            x.Daemon = True
            x.start()
            CURRENT_PORT += 1
            
    #Gives The Syntax Incase Of an error   
    else:
        print("\nERROR INVALID SYNTAX.\n")
        print("--------------------------------------------------------------------------------\n")
        print("Syntax: \"python portscanner.py targetIP startingPort endingPORT\"\n\n")
        sys.exit()

except:
    print("\nERROR INVALID SYNTAX.\n")
    print("--------------------------------------------------------------------------------\n")
    print("Syntax: \"python portscanner.py targetIP startingPort endingPORT\"\n\n")
    sys.exit()
