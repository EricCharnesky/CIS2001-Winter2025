from unit import Unit

class Calvary(Unit):

    ATTACK_POWER = 5
    RANGE = 5
    HIT_POINTS = 10
    MAX_MOVE = 10

    def __init__(self, x_position, y_position, team):
        super().__init__(self.ATTACK_POWER, self.HIT_POINTS, x_position, y_position, team, range = self.RANGE, max_move=self.MAX_MOVE)
