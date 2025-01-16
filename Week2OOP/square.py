
from typing import override

from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, name):
        super().__init__(name)

    @override
    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)

    @override
    def set_width(self, width):
        self.set_length(width)

    @override
    def set_side_length(self, side_index, length):
        self.set_width(length)
        self.set_length(length)