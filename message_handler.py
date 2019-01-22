from model import NeuralNetworkInput
from neural_network import NeuralNetwork
from message_pb2 import *


class MessageHandler:

    def __init__(self, nn: NeuralNetwork):
        self.nn = nn

    def on_message(self, m: Message) -> Message:
        # print("type: " + str(m.__str__()))
        if m.type is LEARN:
            for experience in m.request.experiences:
                self.nn.learn(NeuralNetworkInput.from_proto(experience.state), experience.target)
            m.Clear()
        elif m.type is GETVALUE:
            states = [NeuralNetworkInput.from_proto(experience.state) for experience in m.request.experiences]
            values = self.nn.get_values(states)
            m.Clear()
            m.response.values.extend(values)
        elif m.type is CONFIG:
            self.nn.is_learning_mode = m.request.config.isTraining
            m.Clear()

        m.type = RESPONSE  # this is important since the client cannot handle empty payloads

        return m
