class Polygon:

    def __init__(self, name, number_of_sides):
        self.name = name # not protected because we just don't care

        #self.number_of_sides = number_of_sides

        # protected to ensure valid lengths
        self._side_lengths = []
        for side in range(number_of_sides):
            self._side_lengths.append(0)

    def get_number_of_sides(self):
        return len(self._side_lengths)

    def set_side_length(self, side_index, length):
        if length < 0:
            raise ValueError("invalid length")
        self._side_lengths[side_index] = length

    # returning a copy so they can't change it
    def get_side_lengths(self):
        return self._side_lengths[:]

    def get_side_length(self, side_index):
        return self._side_lengths[side_index]

    def get_perimeter(self):
        return sum(self._side_lengths)




