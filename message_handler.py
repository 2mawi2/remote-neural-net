from model import NeuralNetworkInput
from neural_network import NeuralNetwork
from message_pb2 import *


class MessageHandler:

    def __init__(self, nn: NeuralNetwork):
        self.nn = nn

    def on_message(self, m: Message) -> Message:
        # print("type: " + str(m.__str__()))
        if m.type is LEARN:
            state = NeuralNetworkInput.from_proto(m.request.state)
            self.nn.learn(state, m.request.target)
            m.Clear()
        elif m.type is GETVALUE:
            state = NeuralNetworkInput.from_proto(m.request.state)
            value = self.nn.get_value(state)
            m.Clear()
            m.response.value = value
        elif m.type is CONFIG:
            self.nn.is_learning_mode = m.request.config.isTraining
            m.Clear()

        m.type = RESPONSE  # this is important since the client cannot handle empty payloads

        return m
