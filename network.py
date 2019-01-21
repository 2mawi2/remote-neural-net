import socket

from message_handler import MessageHandler
from neural_network import NeuralNetwork

HOST = "0.0.0.0"  # "127.0.0.1"  # localhost
PORT = 5555

nn = NeuralNetwork()

message_handler = MessageHandler(nn=nn)


def calculation():
    return str.encode("calculated")


def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # tcp
        s.bind((HOST, PORT))
        s.listen(1)
        s.settimeout(30.0)  # if no agent connects within 10 seconds -> timeout
        conn, addr = s.accept()
        # conn.settimeout(3.0)  # if no message response within 3 seconds -> timeout
        print(f"Agent connected.")

        while conn:
            while True:
                data = conn.recv(4096, socket.MSG_WAITALL)


                if not data:
                    break

                result = message_handler.on_message(data)

                conn.send(result)

        print(f"Agent disconnected.")

        conn.close()


if __name__ == '__main__':
    try:
        receive()
    finally:
        nn.save_model()
