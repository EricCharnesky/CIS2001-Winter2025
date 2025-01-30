from infantry import Infantry

class Captain(Infantry):

    ATTACK_POWER = 1
    HIT_POINTS = 20

    def __init__(self, x_position, y_position, team):
        super().__init__(x_position, y_position, team, attack_power=self.ATTACK_POWER, hit_points=self.HIT_POINTS)

    def attack(self, target):
        if self._team == target.get_team() and self._is_within_range(target):
            target.damage(-target.get_max_hit_points())

