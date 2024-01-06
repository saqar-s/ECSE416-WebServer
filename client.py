import socket
import argparse

#default argument values
default_host= '127.0.0.1'
default_port= 12345
# the amount of time the client will wait for a response before exiting
default_timeout= 5
default_file = './text.txt'


def clientSocket(host, port, filename: str, timeout):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(timeout)
    
    try:
        client_socket.connect((host, port))  
        client_socket.send(filename.encode())
        #for testing:
        #HTTP_request_response = client_socket.recv(1024).decode()
        #print('Server HTTP response:', HTTP_request_response)
        client_socket.close()
        print("Socket successfully closed")
        exit(1) 
    except (socket.error):
        print("Could not connect to server")
        print("terminating program")
        client_socket.close()
        exit(1)

def __main__():
    parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parse.add_argument("host", type=str,default=default_host, help="IP address")
    parse.add_argument("port", type=int, default=default_port, help="port number")
    parse.add_argument("filename", type=str, default=default_file, help="file name to query for")
    parse.add_argument("-timeout", type=int, required=False, default=default_timeout, help="amount of time the client will wait for a response")

    arguments = parse.parse_args()
    host = arguments.host
    port = arguments.port
    filename = arguments.filename
    timeout = arguments.timeout
   
    
    clientSocket(host, port, filename, timeout)
    
if __name__ == "__main__":
    print("Starting the software...")
    __main__() 




