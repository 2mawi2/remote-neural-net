import numpy as np


class NeuralNetworkInput:
    angleBallGoal: float
    angleAttackerBall: float
    angleDefenderBall: float
    angleAttacker: float
    angleDefender: float

    distanceBallGoal: float
    distanceAttackerBall: float
    distanceDefenderBall: float

    velAttackerX: float
    velAttackerY: float
    velDefenderX: float
    velDefenderY: float
    velBallX: float
    velBallY: float

    def get_state(self) -> [float]:
        return [
            self.angleBallGoal,
            self.angleAttackerBall,
            self.angleDefenderBall,
            # self.angleAttacker,
            self.angleDefender,

            self.distanceBallGoal,
            self.distanceAttackerBall,
            self.distanceDefenderBall,

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
        i.angleBallGoal = state.angleBallGoal
        i.angleAttackerBall = state.angleAttackerBall
        i.angleDefenderBall = state.angleDefenderBall
        i.angleAttacker = state.angleAttacker
        i.angleDefender = state.angleDefender

        i.distanceBallGoal = state.distanceBallGoal
        i.distanceAttackerBall = state.distanceAttackerBall
        i.distanceDefenderBall = state.distanceDefenderBall

        i.velAttackerX = state.velAttackerX
        i.velAttackerY = state.velAttackerY
        i.velDefenderX = state.velDefenderX
        i.velDefenderY = state.velDefenderY
        i.velBallX = state.velBallX
        i.velBallY = state.velBallY
        return i
