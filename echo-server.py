import socket

HOST = '127.0.0.1' # Standard loopback interface address(localhost)
PORT = 65432       #Port to listen on (non-privileged ports are >1023)
                                    #TCP is the protocol that will be used to transport msgs in the network
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creates a socket obj. that supports the context mngr
    s.bind((HOST, PORT)) #bind is used to associate the socket with a specific network interface and port #
    s.listen()           #listen() enables a server to accept() connections
    conn, addr = s.accept()     #accept blocks and waits for an incoming connection We have a new socket obj. from accept
    with conn:                  #its the socket that you'll use to communicate w/ the client.
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data) #sends back data.
        print('Done')
#The with statement is used with conn to automatically close the socket at the end of the block.