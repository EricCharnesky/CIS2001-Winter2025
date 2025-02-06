class Dequeue:

    def __init__(self):
        self._data = [None] * 10
        self._front_index = None
        self._back_index = None
        self._number_of_items = 0

    def _ensure_capacity(self):
        if self._number_of_items == len(self._data):
            new_data = [None] * len(self._data) * 2
            new_data_index = 0
            for index_to_copy in range(self._front_index, len(self._data)):
                new_data[new_data_index] = self._data[index_to_copy]
                new_data_index += 1
            if self._back_index < self._front_index:
                for index_to_copy in range(0, self._back_index + 1):
                    new_data[new_data_index] = self._data[index_to_copy]
                    new_data_index += 1
            self._front_index = 0
            self._back_index = self._number_of_items - 1
            self._data = new_data

    # O(1)
    def enqueue_front(self, item):
        self._ensure_capacity()
        if self._front_index is None:
            self._front_index = 0
        if self._back_index is None:
            self._back_index = 0
        else:
            self._front_index -= 1
            if self._front_index == -1:
                self._front_index = len(self._data) - 1
        self._data[self._front_index] = item
        self._number_of_items += 1

    # O(1)
    def enqueue_back(self, item):
        self._ensure_capacity()
        if self._front_index is None:
            self._front_index = 0
        if self._back_index is None:
            self._back_index = 0
        else:
            self._back_index += 1
            if self._back_index == len(self._data):
                self._back_index = 0
        self._data[self._back_index] = item
        self._number_of_items += 1

    # O(1)
    def dequeue_front(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        if self._front_index == len(self._data):
            self._front_index = 0
        self._number_of_items -= 1
        return item

    # O(1)
    def dequeue_back(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        item = self._data[self._back_index]
        self._data[self._back_index] = None
        self._back_index -= 1
        if self._back_index == -1:
            self._back_index = len(self._data) - 1
        self._number_of_items -= 1
        return item

    # O(1)
    def front(self):
        return self._data[0]

    # O(1)
    def __len__(self):
        return self._number_of_items

    # O(1)
    def is_empty(self):
        return self._number_of_items == 0

class CircularQueue:

    def __init__(self):
        self._data = [None] * 10
        self._front_index = None
        self._back_index = None
        self._number_of_items = 0

    def _ensure_capacity(self):
        if self._number_of_items == len(self._data):
            new_data = [None] * len(self._data) * 2
            new_data_index = 0
            for index_to_copy in range(self._front_index, len(self._data)):
                new_data[new_data_index] = self._data[index_to_copy]
                new_data_index += 1
            if self._back_index < self._front_index:
                for index_to_copy in range(0, self._back_index + 1):
                    new_data[new_data_index] = self._data[index_to_copy]
                    new_data_index += 1
            self._front_index = 0
            self._back_index = self._number_of_items - 1
            self._data = new_data


    # O(1)
    def enqueue(self, item):
        self._ensure_capacity()
        if self._front_index is None:
            self._front_index = 0
        if self._back_index is None:
            self._back_index = 0
        else:
            self._back_index += 1
            if self._back_index == len(self._data):
                self._back_index = 0
        self._data[self._back_index] = item
        self._number_of_items += 1

    # O(1)
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        if self._front_index == len(self._data):
            self._front_index = 0
        self._number_of_items -= 1
        return item

    # O(1)
    def front(self):
        return self._data[0]

    # O(1)
    def __len__(self):
        return self._number_of_items

    # O(1)
    def is_empty(self):
        return self._number_of_items == 0


class MemoryEatingQueue:

    def __init__(self):
        self._data = []
        self._front_index = 0

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(1) - trading memory usage for performance
    def dequeue(self):
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        return item

    # O(1)
    def front(self):
        return self._data[0]

class Queue:

    def __init__(self):
        self._data = []

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(n)
    def dequeue(self):
        return self._data.pop(0)

    # O(1)
    def front(self):
        return self._data[0]


class Stack:

    def __init__(self):
        self._data = []

    # O(1)
    def push(self, item):
        self._data.append(item)

    # O(1)
    def pop(self):
        return self._data.pop()

    # O(1)
    def peek(self):
        return self._data[-1]

    # O(1)
    def __len__(self):
        return len(self._data)

    # O(1)
    def is_empty(self):
        return len(self._data) == 0

circularQueue = CircularQueue()

for number in range(20):
    circularQueue.enqueue(number)

circularQueue.dequeue()
circularQueue.dequeue()
circularQueue.dequeue()

circularQueue.enqueue(20)
circularQueue.enqueue(21)
circularQueue.enqueue(22)
circularQueue.enqueue(23)

while not circularQueue.is_empty():
    print(circularQueue.dequeue())


deck = Dequeue()

deck.enqueue_front(1)
deck.enqueue_back(2)
deck.enqueue_front(0)
deck.enqueue_back(3)

deck.dequeue_back()

deck.enqueue_front(-1)
deck.enqueue_back(4)

while not deck.is_empty():
    print(deck.dequeue_back())