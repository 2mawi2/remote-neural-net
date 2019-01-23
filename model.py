import numpy as np


class NeuralNetworkInput:
    ballVelX: float
    ballVelY: float
    distanceDefenderAttacker: float
    distanceGoalBall: float
    distanceBallAttacker: float
    defenderVelX: float
    defenderVelY: float
    attackerVelX: float
    attackerVelY: float
    attackerAngleToBall: float
    defenderAngleToBall: float
    strategicAngle: float

    def get_state(self) -> [float]:
        return [
            self.ballVelX,
            self.ballVelY,
            self.distanceDefenderAttacker,
            self.distanceGoalBall,
            self.distanceBallAttacker,
            self.defenderVelX,
            self.defenderVelY,
            self.attackerVelX,
            self.attackerVelY,
            self.attackerAngleToBall,
            self.defenderAngleToBall,
            self.strategicAngle,
        ]

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NeuralNetworkInput) is False:
            return False
        return np.array_equal(self.get_state(), o.get_state())

    @staticmethod
    def from_proto(state):
        i = NeuralNetworkInput()
        i.ballVelX = state.ballVelX
        i.ballVelY = state.ballVelY
        i.distanceDefenderAttacker = state.distanceDefenderAttacker
        i.distanceGoalBall = state.distanceGoalBall
        i.distanceBallAttacker = state.distanceBallAttacker
        i.defenderVelX = state.defenderVelX
        i.defenderVelY = state.defenderVelY
        i.attackerVelX = state.attackerVelX
        i.attackerVelY = state.attackerVelY
        i.attackerAngleToBall = state.attackerAngleToBall
        i.defenderAngleToBall = state.defenderAngleToBall
        i.strategicAngle = state.strategicAngle
        return i
