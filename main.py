from http import client
import socket

PORT = 3004
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('started on {PORT}'.format(PORT = PORT))
server.bind(('127.0.0.1', PORT))
server.listen(5)
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)
HEADERS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
res = 'hello!\r\n'.encode('utf-8')
client_socket.send(HEADERS + res + data.encode('utf-8'))
print('finish process')