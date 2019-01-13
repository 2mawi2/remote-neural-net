class NeuralNetworkInput:
    def __init__(self,
                 ball_vel_x: float,
                 ball_vel_y: float,
                 player_vel_x: float,
                 player_vel_y: float,
                 distance: float,
                 ang_to_ball: float):
        self.ang_to_ball = ang_to_ball
        self.distance = distance
        self.player_vel_y = player_vel_y
        self.player_vel_x = player_vel_x
        self.ball_vel_y = ball_vel_y
        self.ball_vel_x = ball_vel_x

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


class LearnRequest:
    def __init__(self,
                 nn_input: NeuralNetworkInput,
                 value: float):
        self.value = value
        self.input = nn_input
