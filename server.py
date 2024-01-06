#server.py application
#this application does not take any argument and it should be followed by running client.py
#Lab 1 ECSE 416
import socket
import os
import matplotlib.pyplot as plt
import io

default_host= '127.0.0.1'
default_port= 12345
HTTP_error= 'HTTP 404 not found'
HTTP_working = 'HTTP 200 OK'

#function to get the content type of a file
def get_file_extension(file:str):
    if (file.endswith('.txt')):
        content_type = 'text/html'
    elif(file.endswith('.jpg') or file.endswith('jpeg') or file.endswith('png')):
        content_type = 'image'
    elif (file.endswith('.mp3')):
        content_type = 'audio'
    elif (file.endswith('.mp4')):
        content_type = 'video'
    return content_type


def __main__():
    #help from https://www.internalpointers.com/post/making-http-requests-sockets-python
    #following commands were also given during lab session
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((default_host, default_port))
    #from book:
    #the server listens for TCP connection requests from the client. The parameter specifies the maximum number of queued connections (at least 1)
    server_socket.listen(1)
    while True:
        #from book:
        #program invokes the accept() method for serverSocket, which creates a new socket in the server, called connectionSocket
        try:
            connectionSocket, _ = server_socket.accept()
            print("Connection: OK")
            http_request_file = connectionSocket.recv(1024).decode()
            print("Request message sent.")
        except (socket.error):
            print("Connection: Not OK")
            print("terminating program")
            server_socket.close()
            exit(1)

        if (os.path.exists(http_request_file)):
            #sends the HTTP response with the status code either working or not to the client. this is how the server communicates with the client
            connectionSocket.send(http_request_file.encode())
            print('Server HTTP response:', HTTP_working)
            contentType = get_file_extension(http_request_file)
            print('Content-Type: ',contentType)
            
            if(contentType =='text/html'):
                with open(http_request_file,'r') as f:
                    content = f.read()
                    print(content)

            elif(contentType == 'image'):
                with open(http_request_file,'rb') as f:
                    content = f.read()
                    #if we don't do the following, the program will just read the bytes and will not display the image
                    img = plt.imread(io.BytesIO(content), format=(os.path.splitext(http_request_file)[1].lower()))
                    plt.imshow(img)
                    plt.show()
            else:
                with open(http_request_file,'rb') as f:
                    content = f.read()
                    dir_name = 'saved_content'
                    if not os.path.exists(dir_name):
                        os.makedirs('saved_content')
                    
                    with open(os.path.join(dir_name, http_request_file),'wb') as new:
                        new.write(content)
                 
                
        else:
            connectionSocket.send(HTTP_error.encode())
            print('Server HTTP response:', HTTP_error)
            print(HTTP_error)
        
        server_socket.close()
        print("Socket successfully closed")
        exit(1)
        
if __name__ == "__main__":
    print("Starting the software...")
    __main__()        
        



        
    


