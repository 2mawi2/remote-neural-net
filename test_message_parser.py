from unittest import TestCase
from message_parser import MessageParser, Method
from model import NeuralNetworkInput


class TestMessageParser(TestCase):
    def test_should_parse_method_learn(self):
        parser = MessageParser()
        result = parser.parse_input(b"1 payload NULL")
        self.assertEqual(result.method, Method.LEARN)

    def test_should_parse_method_get_value(self):
        parser = MessageParser()
        result = parser.parse_input(b"0 payload NULL")
        self.assertEqual(result.method, Method.GETVALUE)

    def test_should_parse_nn_input(self):
        parser = MessageParser()
        result = parser.parse_input(b"0 1.7733:8.8899:1.7733:1.7733:1.7733:1.7733 0.8877").inp

        self.assertEqual(result.ball_vel_x, 1.7733)
        self.assertEqual(result.ball_vel_y, 8.8899)
        self.assertEqual(result.player_vel_x, 1.7733)
        self.assertEqual(result.player_vel_y, 1.7733)
        self.assertEqual(result.distance, 1.7733)
        self.assertEqual(result.ang_to_ball, 1.7733)

    def test_should_parse_target(self):
        parser = MessageParser()
        result = parser.parse_input(b"0 inv 0.8877")
        self.assertEqual(result.target, 0.8877)

    def test_should_parse_target_as_optional(self):
        parser = MessageParser()
        result = parser.parse_input(b"0 inv NULL")
        self.assertEqual(result.target, None)
