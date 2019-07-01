#!/usr/bin/env python3

import socket
import sys

path = sys.argv[1]  # get socket path

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
  s.connect(path)

  # data to be send
  detail = {
    'id': 99,
    'type': 'sign_transfer',
    'from_address': '0xEeC9B9721Fe2458a5D112B7A47a9f03dBe749634',
    'to_address': '0x7A834a2dbFB6A9e965761b6a4b32a242d7C85506',
    'amount': 50000000000000 # in wei
  }
  #print(send)
  s.sendall(str(detail).encode())
  data = s.recv(1024)
  s.close()

print(repr(data))