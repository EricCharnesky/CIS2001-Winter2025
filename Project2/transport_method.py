class TransportMethod:

    TRAIN_TIME_MULTIPLIER = 1
    PLANE_TIME_MULTIPLIER = 5

    def __init__(self, number, expected_number_of_items, transport_multiplier):
        self.number = number
        self.expected_number_of_items = expected_number_of_items
        self.time_when_fully_loaded = 0
        self.current_number_of_items = 0
        self.transport_multiplier = transport_multiplier

    def add_item(self, current_time):
        current_time += self.number * self.transport_multiplier
        self.current_number_of_items += 1
        if self.current_number_of_items == self.expected_number_of_items:
            self.time_when_fully_loaded = current_time
        return current_time + self.number * self.transport_multiplier
