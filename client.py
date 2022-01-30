import socket


# Main function
if __name__ == "__main__":

        # Host And Port For Server
        HOST = '192.168.56.110'
        PORT = 8888

        # OK Message
        messageOK= "ok"

        # Client socket
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to server
        clientSock.connect(('192.168.56.110', 8888))

        print("Connect to localhost on port: ", 8888)
        print("Please wait for all players to join...")

        # Send to server upon connecting
        clientSock.sendall(bytes("play",'utf-8'))

        # Get the welcome message
        resp = clientSock.recv(2048)
        print(resp.decode("utf-8"))

        # Send the "ok" after welcome message
        clientSock.sendall(bytes(messageOK,'utf-8'))

        while(1):

                # Receive response
				
                try:
                        resp = clientSocket.recv(2048)
						
                except (BrokenPipeError,ConnectionResetError):
                        break

                # Validate the response
				
                if resp != b'':

                        # Check if the server instructed to wait or to make a move
						
                        if resp.decode("utf-8") == "wait":
						    print("Wait! Other player make a move now.........")
                                message = messageOK
								
                        elif resp.decode("utf-8") == "go":
                                message = input("Enter your letter: ")								
                        else: # Generic reponse for not a "wait" or a "go"
                                print(resp.decode("utf-8"))
                                message = messageOK


                # Send response message; aka the player's guess or an "ok" message
				
                try:
                        clientSock.sendall(bytes(message,'utf-8'))
						
                except (BrokenPipeError,ConnectionResetError,OSError):
                        break

                if message == "/q":
                        print("Oopps sorry our pirates have other duties to attend....See you!")
                        break

        clientSock.close()
