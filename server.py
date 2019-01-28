#!/usr/bin/env python

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
        self.socket.listen(2)
        self.conn, self.addr = self.socket.accept()
        self.connection = True
        print("Agent connected")

    def signal_handler(self, signal, frame):
        print(f"saving model...")
        nn.save_model()
        print("SIGINT caught, exiting ...")
        if self.connection:
            self.connection = False
        self.conn.close()

    def run(self):
        while self.connection:

            # Listen for client request with 5 characters header
            data_hdr = self.conn.recv(5)

            if not data_hdr:
                break
            sz = int(data_hdr)

            chunks = []
            bytes_recv = 0
            while bytes_recv < sz:
                chunk = self.conn.recv(min(sz - bytes_recv, 65_535))
                if chunk == '':
                    raise RuntimeError("socket connection broken")
                chunks.append(chunk)
                bytes_recv += len(chunk)
            data = b''.join(chunks)

            if sz != len(data):
                print(f"header size: {sz} , actual size: {len(data)}")
                break

            try:
                self.message.ParseFromString(data)
            except:
                print(f"header size: {sz} , actual size: {len(data)}")

            self.connection = not self.message.endConnection
            self.data_m.endConnection = False

            self.data_m = message_handler.on_message(self.message)
            s = self.data_m.SerializeToString()
            total_len = 5 + self.data_m.ByteSize()
            self.conn.sendall(bytes(str(total_len).zfill(5), "utf-8") + s)
            time.sleep(0.001)

        print("Closing socket ...")
        self.conn.close()


if __name__ == '__main__':
    client = tcp_server()

    try:
        client.run()
    except Exception as e:
        print(f"server process ended. Reason: {str(e)}")
    finally:
        print(f"saving model...")
        nn.save_model()
