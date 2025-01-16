from polygon import Polygon
import math

class Triangle(Polygon):

    def __init__(self, name):
        super().__init__(name, 3)

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter
                 *(semi_perimeter-self.get_side_length(0))
                * (semi_perimeter-self.get_side_length(1) )
                * (semi_perimeter - self.get_side_length(2) ) )
