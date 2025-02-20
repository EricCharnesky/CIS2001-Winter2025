class DoublyLinkedList:

    class Node:

        def __init__(self, data, next = None, previous = None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._dummy_node = self.Node(None)
        self._dummy_node.next = self._dummy_node
        self._dummy_node.previous = self._dummy_node
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return len(self) == 0

    def _add_node(self, data, next, previous):
        new_node = self.Node(data, next=next, previous=previous)
        new_node.next.previous = new_node
        new_node.previous.next = new_node

    # O(1)
    def add_front(self, data):
        self._add_node(data, next=self._dummy_node.next, previous=self._dummy_node)
        self._number_of_items += 1

    # O(1)
    def add_back(self, data):
        self._add_node(data, next=self._dummy_node, previous=self._dummy_node.previous)
        self._number_of_items += 1

    def _remove_node(self, node):
        data = node.data
        node.next.previous = node.previous
        node.previous.next = node.next
        return data

    # O(1)
    def remove_front(self):
        if self.is_empty():
            raise ValueError("Empty!")

        self._number_of_items -= 1

        return self._remove_node(self._dummy_node.next)

    # O(1)
    def remove_back(self):
        if self.is_empty():
            raise ValueError("Empty!")

        self._number_of_items -= 1
        return self._remove_node(self._dummy_node.previous)

    # O(n)
    def find(self, data):
        current_node = self._dummy_node.next

        while current_node != self._dummy_node:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False

    # O(n)
    def __getitem__(self, index):
        if index < 0 or index >= self._number_of_items:
            raise IndexError()
        current_index = 0
        current_node = self._dummy_node.next

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node.data

    # O(n)
    def __setitem__(self, index, item):
        # TODO - if index is closer to the number of items, start at the back node and walk backwards
        if index < 0 or index >= self._number_of_items:
            raise IndexError()
        current_index = 0
        current_node = self._dummy_node.next

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        current_node.data = item