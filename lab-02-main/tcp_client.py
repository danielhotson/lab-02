"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

IPC = "10.0.2.15"
IPRPI = "192.168.70.4"
PORT = 1500

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    	s.connect((IPRPI, PORT))
    	s.sendall(b"hey")
    	data = s.recv(1024)
   print(f"Received {data!r}")
   
    	   
    # TODO: Get user input and send it to the server using your TCP socket
    # TODO: Receive a response from the server and close the TCP connection
   pass
   
   input('abcd')


if __name__ == '__main__':
    main()
    
