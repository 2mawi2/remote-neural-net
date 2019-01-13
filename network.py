import socket

from message_handler import MessageHandler
from neural_network import NeuralNetwork
from message_parser import MessageParser

HOST = "127.0.0.1"  # localhost
PORT = 5555

nn = NeuralNetwork()
parser = MessageParser()

message_handler = MessageHandler(nn=nn, parser=parser)


def calculation():
    return str.encode("calculated")


def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # tcp
        s.bind((HOST, PORT))
        s.listen(10)
        s.settimeout(10.0)
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print(f"Agent connected.")

        while conn:
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                result = message_handler.on_message(data)

                conn.sendall(result)

        print(f"Agent disconnected.")


if __name__ == '__main__':
    receive()
