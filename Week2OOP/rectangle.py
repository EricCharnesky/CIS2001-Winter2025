from typing import override

from polygon import Polygon

class Rectangle(Polygon):

    def __init__(self, name):
        super().__init__(name, 4)

    @override
    def set_side_length(self, side_index, length):
        # shortcut for not 0
        if side_index % 2:
            super().set_side_length(1, length)
            super().set_side_length(3, length)
        else:
            super().set_side_length(0, length)
            super().set_side_length(2, length)

    def get_area(self):
        return self.get_side_length(0) * self.get_side_length(1)

    def set_length(self, length):
        self.set_side_length(0, length)

    def get_length(self):
        return self.get_side_length(0)

    def set_width(self, width):
        self.set_side_length(1, width)

    def get_width(self):
        return self.get_side_length(1)
