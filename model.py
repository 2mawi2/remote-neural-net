class NeuralNetworkInput:
    ang_to_ball: float
    distance: float
    player_vel_y: float
    player_vel_x: float
    ball_vel_y: float
    ball_vel_x: float

    def get_state(self) -> [float]:
        return [
            self.ball_vel_x,
            self.ball_vel_y,
            self.player_vel_x,
            self.player_vel_y,
            self.distance,
            self.ang_to_ball,
        ]

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NeuralNetworkInput) is False:
            return False

        return self.ball_vel_x == o.ball_vel_x \
               and self.ball_vel_y == o.ball_vel_y \
               and self.player_vel_x == o.player_vel_x \
               and self.player_vel_y == o.player_vel_y \
               and self.distance == o.distance \
               and self.ang_to_ball == o.ang_to_ball

    @staticmethod
    def from_proto(state):
        i = NeuralNetworkInput()
        i.ang_to_ball = state.angleToBall
        i.distance = state.distance
        i.player_vel_y = state.playerVelY
        i.player_vel_x = state.playerVelX
        i.ball_vel_y = state.ballVelX
        i.ball_vel_x = state.ballVelY
        return i
