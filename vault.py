#!/usr/local/bin/python3.7

import socket
import ast
import Transaction
import sys
import os

path = sys.argv[1]  # get socket path

# remove path if exist
try:
    os.unlink(path)
except FileNotFoundError:
    pass

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
  s.bind(path)
  while True:
    s.listen(1)
    conn, addr = s.accept()
    with conn:
      print('Connected by', path)
      while True:
        data = conn.recv(1024)
        if(data):
          received_str = data.decode('utf-8')
          try:
            received_dict = ast.literal_eval(received_str)
            
            # get PK
            with open(received_dict['from_address'], 'r') as file:
              pk = file.read()

            tx = Transaction.Transaction(pk, received_dict['to_address'], received_dict["amount"])
            result = tx.sign()
            response = {
              'id': received_dict['id'],
              'tx': result
            }
            print(result)
          except ValueError:
            print("Value Error")
          except SyntaxError:
            print("SyntaxError")
            
          if(not data):
            break

          conn.sendall(str(response).encode())
          break
          
