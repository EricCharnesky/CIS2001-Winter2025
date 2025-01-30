from unit import Unit

class Infantry(Unit):

    MAX_MOVE = 5
    ATTACK_POWER = 5
    HIT_POINTS = 5

    def __init__(self, x_position, y_position, team, hit_points = HIT_POINTS, attack_power = ATTACK_POWER):
        super().__init__(attack_power, hit_points, x_position, y_position, team, max_move=5)

