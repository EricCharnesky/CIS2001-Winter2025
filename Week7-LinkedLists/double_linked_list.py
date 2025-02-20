class DoublyLinkedList:

    class Node:

        def __init__(self, data, next = None, previous = None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return len(self) == 0

    # O(1)
    def add_front(self, data):
        if self._front is None:
            self._front = self.Node(data)
            self._back = self._front
        else:
            self._front.previous = self.Node(data, next=self._front)
            self._front = self._front.previous
        self._number_of_items += 1

    # O(1)
    def add_back(self, data):
        if self._front is None:
            self._front = self.Node(data)
            self._back = self._front
        else:
            self._back.next = self.Node(data, previous=self._back)
            self._back = self._back.next
        self._number_of_items += 1

    # O(1)
    def remove_front(self):
        if self.is_empty():
            raise ValueError("Empty!")
        data = self._front.data
        self._front = self._front.next


        if self._front is None:
            self._back = None
        else:
            self._front.previous = None

        self._number_of_items -= 1
        return data

    # O(1)
    def remove_back(self):
        if self.is_empty():
            raise ValueError("Empty!")
        data = self._back.data
        self._back = self._back.previous


        if self._back is None:
            self._front = None
        else:
            self._back.next = None

        self._number_of_items -= 1
        return data

    # O(n)
    def find(self, data):
        current_node = self._front

        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False

    # O(n)
    def __getitem__(self, index):
        if index < 0 or index >= self._number_of_items:
            raise IndexError()
        current_index = 0
        current_node = self._front

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node.data

    # O(n)
    def __setitem__(self, index, item):
        if index < 0 or index >= self._number_of_items:
            raise IndexError()
        current_index = 0
        current_node = self._front

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        current_node.data = item