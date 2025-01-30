from unit import Unit

class Artillery(Unit):

    ATTACK_POWER = 10
    RANGE = 10
    HIT_POINTS = 1
    MAX_MOVE = 1

    def __init__(self,  x_position, y_position, team):
        super().__init__(self.ATTACK_POWER, self.HIT_POINTS, x_position, y_position, team, self.RANGE, max_move=1)

