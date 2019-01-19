from model import NeuralNetworkInput
from neural_network import NeuralNetwork
from message_pb2 import Message


class MessageHandler:

    def __init__(self, nn: NeuralNetwork):
        self.nn = nn

    def on_message(self, data: bytes) -> bytes:
        print("message")
        m = Message()

        m.ParseFromString(data)
        print("type: " + m.type)
        if m.type is Message.LEARN:
            state = NeuralNetworkInput.from_proto(m.request.state)
            self.nn.learn(state, m.request.target)
            m.Clear()
            m.type = Message.LEARN
        elif m.type is Message.GETVALUE:
            state = NeuralNetworkInput.from_proto(m.request.state)
            value = self.nn.get_value(state)
            m.Clear()
            m.response.value = value
            m.type = Message.GETVALUE

        return m.SerializeToString()
