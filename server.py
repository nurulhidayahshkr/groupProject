import socket
from game  import *

# Call main function
if __name__ == "__main__":


        # Maximum client can be connect
        MAX_CLI = 2

        # Number of connections
        conn = 0

        # Server socket
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind socket
        serverSock.bind(("",8888))

        # Queue up to MAX_CLI connections
        serverSock.listen(MAX_CLI)

        print("Server listening at localhost on port: ", 8888)

        (welcomeMessage,ship,word) = setupShip()

        # Establish 2 connections; one for each player and then begin the game
        while(conn < 2):
                if conn == 0:
                        # Accept connection
                        (clientSock, addr) = serverSock.accept()
                else:
                        # Accept connection
                        (clientSock2, addr) = serverSock.accept()

                conn += 1

                print("Connected by ", addr)

        try:
                # Get the message from the client
                resp = clientSock.recv(2048)
                resp2 = clientSock2.recv(2048)

                # Send welcome message
                clientSock.sendall(bytes(welcomeMessage,'utf-8'))
                clientSock2.sendall(bytes(welcomeMessage,'utf-8'))

                # Receive the "ok"
                resp = clientSock.recv(2048)
                resp2 = clientSock2.recv(2048)

        except BrokenPipeError:
                serverSock.close()

        else:
                turn = 0
                msg = ""

                while(1):

                        if turn % 2 == 0:
                                # Notify clients to "wait" or "go"
                                clientSock.sendall(bytes("go",'utf-8'))
                                clientSock2.sendall(bytes("wait",'utf-8'))

                                # Get the message from the clients
                                resp = clientSock.recv(2048)
                                clientSock2.recv(2048)

                                # Checks if client exited and closed the connection
                                if resp.decode("utf-8") == "/q":
                                        clientSock2.sendall(bytes("Another player quit..Game over!",'utf-8'))
                                        resp = clientSock2.recv(2048)
                                        break

                        else:
                                # Notify clients to "wait" or "go"
                                clientSock.sendall(bytes("wait",'utf-8'))
                                clientSock2.sendall(bytes("go",'utf-8'))

                                 # Get the message from the client
                                resp = clientSock2.recv(2048)
                                clientSock.recv(2048)

                                # Checks if client exited and closed the connection
                                if resp.decode("utf-8") == "/q":
                                        clientSock.sendall(bytes("Another player quit..Game over!",'utf-8'))
                                        resp = clientSock.recv(2048)
                                        break

                        if startShipSink(resp.decode("utf-8"),word,ship):
                                msg = "\nAHOY! WELL DONE!!\nYour guess was: " + resp.decode("utf-8") + "\n\nThe Secret Word: " + ship.getSolve()

                                if ship.gameOver():
                                        msg = "\n*********!!!!********\nYou won and your ship didn't sink!!\nThe secret word was: " + word + "\n\n"
                                        clientSock.sendall(bytes(msg,'utf-8'))
                                        clientSock2.sendall(bytes(msg,'utf-8'))
                                        break
                        else:

                                if ship.getWaterFill() < 12:
                                        msg = "\nWRONG! THAT'S NOT THE WORD!!!\n" + ship.getSinkShip() + "\n\nYour guess was: " + resp.decode("utf-8") + "\n\nThe Secret Word: " + ship.getSolve()

                                else:

                                        msg = ship.getSinkShip() + "\n\nYour Guess was: " + resp.decode("utf-8") + "\n\nYou lost! Oh,no! The pirates filled up the ship full of water and sank!.. \n\nThe secret word was: " + word + "\n"
                                        clientSock.sendall(bytes(msg,'utf-8'))
                                        clientSock2.sendall(bytes(msg,'utf-8'))
                                        break


                        # Send response message to both clients
                        clientSock.sendall(bytes(msg,'utf-8'))
                        clientSock2.sendall(bytes(msg,'utf-8'))

                        # Receive message back from client to send out next prompt
                        clientSock.recv(2048)
                        clientSock2.recv(2048)
                        
                        turn += 1

                serverSock.close()

