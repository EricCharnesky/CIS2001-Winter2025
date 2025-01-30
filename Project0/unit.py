class Unit:

    def __init__(self, attack_power, hit_points, x_position, y_position, team, range = 2**.5, max_move = 1):
        self._attack_power = attack_power
        self._hit_points = hit_points
        self._max_hit_points = hit_points
        self._range = range
        self._x_position = x_position
        self._y_position = y_position
        self._team = team
        self._max_move = max_move

    def is_alive(self):
        return self._hit_points > 0

    # umgpt
    # generate get functions for this class
    # class Unit:
    #
    #     def __init__(self, attack_power, hit_points, range, x_position, y_position, team):
    #         self._attack_power = attack_power
    #         self._hit_points = hit_points
    #         self._range = range
    #         self._x_position = x_position
    #         self._y_position = y_position
    #         self._team = team

    def get_attack_power(self):
        return self._attack_power

    def get_hit_points(self):
        return self._hit_points

    def get_range(self):
        return self._range

    def get_x_position(self):
        return self._x_position

    def get_y_position(self):
        return self._y_position

    def get_team(self):
        return self._team

    def get_max_hit_points(self):
        return self._max_hit_points

    def move(self, x_move, y_move):
        if x_move and y_move:
            raise ValueError("Unable to move both x and y")
        if x_move > self._max_move or y_move > self._max_move:
            raise ValueError("Unable to move more than 5")
        self._x_position += x_move
        self._y_position += y_move

    def damage(self, points):
        self._hit_points -= points
        if self._hit_points < 0:
            self._hit_points = 0
        if self._hit_points > self._max_hit_points:
            self._hit_points = self._max_hit_points

    def _should_attack(self, target):
        return self._team == 'chaotic' or self._team != target.get_team()


    def _is_within_range(self, target):
        return (( self._x_position - target.get_x_position() )**2 +
            (self._y_position - target.get_y_position()) ** 2)**.5 <= self._range

    def attack(self, target):
        if self._should_attack(target) and self._is_within_range(target):
            target.damage(self._attack_power)