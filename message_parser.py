from model import NeuralNetworkInput
from enum import Enum


class Method(Enum):
    LEARN = 1,
    GETVALUE = 2,


class InputMessage:
    def __init__(self, method: Method, inp: NeuralNetworkInput, target: float):
        self.method = method
        self.inp = inp
        self.target = target


class OutputMessage:
    def __init__(self, value: float):
        self.value = value


class MessageParser:
    def _parse_method(self, param: str) -> Method:
        if param == "0":
            return Method.GETVALUE
        elif param == "1":
            return Method.LEARN
        else:
            raise ValueError(f"method: {param} is invalid")

    def _parse_inp(self, param) -> NeuralNetworkInput:
        elements = param.split(":")

        if len(elements) < 6:
            return None

        return NeuralNetworkInput(
            ball_vel_x=float(elements[0]),
            ball_vel_y=float(elements[1]),
            player_vel_x=float(elements[2]),
            player_vel_y=float(elements[3]),
            distance=float(elements[4]),
            ang_to_ball=float(elements[5])
        )

    def _parse_target(self, param) -> float:
        return float(param) if param != "NULL" else None

    def parse_input(self, data: bytes) -> InputMessage:
        # CONN_ACTIVE METHOD
        string = data.decode("ASCII")
        params = string.split(" ")

        return InputMessage(
            method=self._parse_method(params[0]),
            inp=self._parse_inp(params[1]),
            target=self._parse_target(params[2])
        )

    def parse_output(self, value) -> bytes:
        return bytes(f'{value:.9f}', encoding="ASCII")

