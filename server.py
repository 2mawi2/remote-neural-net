#!/usr/bin/env python

'''
This is a small TCP server that handles a protobuf communication example.
When a connection is established, the server will:
	- Wait for a client request to be sent
	- Reply with a protobuf message back with dummy XYZ positions of an object
The server will loop until either CTRL+C is pressed (in which case it will cleanly close the socket and exit), or until the client request includes an endConnection=True message
The current version has a small bug making it receive corrupted messages after a few loops. It will be fixed later.
'''

import socket
import struct
import signal
import time

from message_pb2 import *

import numpy as np

from message_handler import MessageHandler
from neural_network import NeuralNetwork

nn = NeuralNetwork()

message_handler = MessageHandler(nn=nn)


class tcp_server:
    def __init__(self):
        self.message = Message()
        self.message.endConnection = False
        self.data_m = Message()
        signal.signal(signal.SIGINT, self.signal_handler)
        tcp_ip = '0.0.0.0'
        port = 5555

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((tcp_ip, port))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        self.connection = True
        print("Agent connected")

    def signal_handler(self, signal, frame):
        print("SIGINT caught, exiting ...")
        if self.connection:
            self.connection = False

    def run(self):
        while self.connection:

            # Listen for client request with 4 characters header
            data_hdr = self.conn.recv(4)

            if not data_hdr:
                break
            sz = int(data_hdr)

            data = self.conn.recv(sz)
            self.message.ParseFromString(data)
            self.connection = not self.message.endConnection
            self.data_m.endConnection = False

            self.data_m = message_handler.on_message(self.message)
            s = self.data_m.SerializeToString()
            total_len = 4 + self.data_m.ByteSize()
            self.conn.sendall(bytes(str(total_len).zfill(4), "utf-8") + s)

        print("Closing socket ...")
        self.conn.close()


if __name__ == '__main__':
    client = tcp_server()

    try:
        client.run()
    except:
        nn.save_model()
