import socket, string


TCP_IP = '127.0.0.1'

TCP_PORT = 3000
BUFFER_SIZE = 1024



message = chr(0x83)+chr(0x10)+chr(0x10)+chr(0xF0)+chr(0x01)+chr(0x01)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

print s.send(message)

s.close
