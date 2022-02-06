from http import client, server
from importlib.resources import path
from pickle import TRUE
import socket
from unittest.mock import patch
from urllib import response

PORT = 3006

def start_server():
  try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('started on {PORT}/tcp...'.format(PORT = PORT))
    server.bind(('127.0.0.1', PORT))
    server.listen(5)
    while TRUE:
      client_socket, address = server.accept()
      data = client_socket.recv(1024).decode('utf-8')
      print(data)
      res = get_response(data)
      client_socket.send(res)
      client_socket.shutdown(socket.SHUT_WR)
  except KeyboardInterrupt:
    server.close()    
    print('finish process')

def get_response(request):
  path = request.split(' ')[1]
  
  # if path != 'users' or 'users.html':
  #   path = 'index'

  HEADERS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
  response = ''
  with open('requests/'+ path + '.html', 'rb') as file:
    response=file.read()
  return HEADERS + response

start_server()  