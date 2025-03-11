from transport_method import TransportMethod
from collections import deque
from stack import Stack


class Dock:

    TRAIN_STACK_HEIGHT_MAX = 5

    def __init__(self, number_of_items_per_train, number_of_items_per_plane, train_items, plane_items):
        self.trains = []

        # adding an empty train so trains are at their index number
        self.trains.append(None)

        for train_number in range(1, len(number_of_items_per_train)+1):
            self.trains.append(TransportMethod(train_number,
                                          number_of_items_per_train[train_number-1],
                                          TransportMethod.TRAIN_TIME_MULTIPLIER))
        self.planes = []
        # adding an empty plane so trains are at their index number
        self.planes.append(None)
        for plane_number in range(1, len(number_of_items_per_plane)+1):
                self.planes.append(TransportMethod(plane_number,
                                              number_of_items_per_plane[plane_number-1],
                                              TransportMethod.PLANE_TIME_MULTIPLIER))


        self.train_items = deque()
        current_stack = Stack()

        for train_item in train_items:
            current_stack.push(train_item)
            if len(current_stack) == self.TRAIN_STACK_HEIGHT_MAX:
                self.train_items.append(current_stack)
                current_stack = Stack()

        # if there wasn't a full stack of 5 left over
        if len(current_stack):
            self.train_items.append(current_stack)

        self.plane_items = deque()
        for plane_item in plane_items:
            self.plane_items.append(plane_item)

    def load_trains(self):
        current_time = 0
        while len(self.train_items):
            current_stack = self.train_items.popleft()
            while len(current_stack):
                train_number = current_stack.pop()
                current_time = self.trains[train_number].add_item(current_time)

    def load_planes(self):
        current_time = 0
        while len(self.plane_items):
            plane_number = self.plane_items.popleft()
            current_time = self.planes[plane_number].add_item(current_time)

    def __str__(self):
        result = ""
        for train in self.trains[1:]:
            result += f'{train.time_when_fully_loaded} '
        result += "\n"
        for plane in self.planes[1:]:
            result += f'{plane.time_when_fully_loaded} '
        result += "\n"
        return result