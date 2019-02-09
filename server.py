#!/usr/bin/env python

import signal
import time
import socket
from threading import Thread, Lock

from message_pb2 import *

from message_handler import MessageHandler

handler_lock = Lock()
keepAlive = True
HEADER_SIZE = 5


class ClientThread(Thread):

    def __init__(self, conn, local_handler: MessageHandler):
        Thread.__init__(self)
        self.conn = conn
        self.message = Message()
        self.message.endConnection = False
        self.data_m = Message()
        self.local_handler = local_handler

    def run(self):
        global keepAlive
        while keepAlive:
            # Listen for client request with 5 characters header

            data_hdr = self.conn.recv(HEADER_SIZE)

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
                print("HEADER SIZE DOES NOT MATCH")
                print(f"header size: {sz} , actual size: {len(data)}")
                break

            try:
                self.message.ParseFromString(data)
            except:
                print("PARSING FAILED")
                print(f"header size: {sz} , actual size: {len(data)}")

            keepAlive = not self.message.endConnection

            self.data_m.endConnection = False

            with handler_lock:
                self.data_m = self.local_handler.on_message(self.message)

            s = self.data_m.SerializeToString()
            total_len = HEADER_SIZE + self.data_m.ByteSize()
            self.conn.sendall(bytes(str(total_len).zfill(5), "utf-8") + s)
            time.sleep(0.001)

        print("Closing socket ...")
        self.conn.close()


class Server:
    def __init__(self, server_handler: MessageHandler):
        signal.signal(signal.SIGINT, self.signal_handler)
        tcp_ip = '0.0.0.0'
        port = 5555

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((tcp_ip, port))

        self.connections = []
        threads = []

        for _ in range(2):
            self.socket.listen(2)

            conn = self.socket.accept()[0]
            self.connections.append(conn)

            print("Agent connected")

            thread = ClientThread(conn, server_handler)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()

        self.connection = True

    def signal_handler(self, signal, frame):
        print(f"saving model...")
        with handler_lock:
            handler.nn.save_model()

        print("SIGINT caught, exiting ...")
        global keepAlive
        if keepAlive:
            keepAlive = False

        for conn in self.connections:
            conn.close()


if __name__ == '__main__':
    handler = MessageHandler.instance()
    is_address_in_use = False
    try:
        server = Server(handler)
    except Exception as e:
        print(f"server process ended. Reason: {str(e)}")
        is_address_in_use = "Address already in use" in str(e)
    finally:
        if not is_address_in_use:
            handler.nn.save_model()
