from neural_network import NeuralNetwork
from message_parser import MessageParser, Method


class MessageHandler:

    def __init__(self, nn: NeuralNetwork, parser: MessageParser):
        self.nn = nn
        self.parser = parser

    def on_message(self, data: bytes) -> bytes:
        result = self.parser.parse_input(data)

        if result.method is Method.LEARN:
            self.nn.learn(result.inp, result.target)
            return b"NONCE"  # we need to return at least one space of bytes
        elif result.method is Method.GETVALUE:
            value = self.nn.get_value(result.inp)
            return self.parser.parse_output(value)

