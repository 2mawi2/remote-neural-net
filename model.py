import numpy as np


class NeuralNetworkInput:
    angleAttackerGoal: float
    angleAttackerBall: float
    angleAttackerDefender: float
    angleAttacker: float
    angleDefender: float

    distanceAttackerGoal: float
    distanceAttackerBall: float
    distanceAttackerDefender: float

    velAttackerX: float
    velAttackerY: float
    velDefenderX: float
    velDefenderY: float
    velBallX: float
    velBallY: float

    def get_state(self) -> [float]:
        return [
            self.angleAttackerGoal,
            self.angleAttackerBall,
            self.angleAttackerDefender,
            self.angleAttacker,
            self.angleDefender,

            self.distanceAttackerBall,
            self.distanceAttackerDefender,

            self.velAttackerX,
            self.velAttackerY,
            self.velDefenderX,
            self.velDefenderY,
            self.velBallX,
            self.velBallY,
        ]

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NeuralNetworkInput) is False:
            return False
        return np.array_equal(self.get_state(), o.get_state())

    @staticmethod
    def from_proto(state):
        i = NeuralNetworkInput()
        i.angleAttackerGoal = state.angleAttackerGoal
        i.angleAttackerBall = state.angleAttackerBall
        i.angleAttackerDefender = state.angleAttackerDefender
        i.angleAttacker = state.angleAttacker
        i.angleDefender = state.angleDefender

        i.distanceAttackerGoal = state.distanceAttackerGoal
        i.distanceAttackerBall = state.distanceAttackerBall
        i.distanceAttackerDefender = state.distanceAttackerDefender

        i.velAttackerX = state.velAttackerX
        i.velAttackerY = state.velAttackerY
        i.velDefenderX = state.velDefenderX
        i.velDefenderY = state.velDefenderY
        i.velBallX = state.velBallX
        i.velBallY = state.velBallY
        return i
