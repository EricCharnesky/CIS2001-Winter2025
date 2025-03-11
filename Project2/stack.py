
# https://github.com/EricCharnesky/CIS2001-Winter2025/blob/main/Week5-StacksAndQueues/main.py
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
