class PositionalCircularDoublyLinkedList:


    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def data(self): # book calls it element
            return self._node.data

        # from book
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)
    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._dummy_node = self.Node(None)
        # dummy_node next is always the first item
        self._dummy_node.next = self._dummy_node

        # dummy_node previous is always the last item
        self._dummy_node.previous = self._dummy_node
        self._number_of_items = 0

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError
        if self is not position._container:
            raise ValueError
        if position._node.next is None:
            raise ValueError
        return position._node


    def _make_position(self, node):
        if node == self._dummy_node:
            return None
        return self.Position(self, node)

    def _add_between(self, data, next_node, previous_node):
        new_node = self.Node(data, next=next_node, previous=previous_node )
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self._number_of_items += 1
        return new_node

    # O(1)
    def first(self):
        return self._make_position(self._dummy_node.next)

    # O(1)
    def last(self):
        return self._make_position(self._dummy_node.previous)

    # O(1)
    def before(self, position):
        node = self._validate(position)
        return self._make_position(node.previous)

    # O(1)
    def after(self, position):
        node = self._validate(position)
        return self._make_position(node.next)

    # O(1)
    def add_after(self, position, data):
        node = self._validate(position)
        return self._make_position(self._add_between(data, previous_node=node, next_node=node.next))

    # O(1)
    def add_before(self, position, data):
        node = self._validate(position)
        return self._make_position(self._add_between(data, next_node=node, previous_node=node.previous))


    def __iter__(self):
        current = self.first()

        while current is not None:
            yield current.data()
            current = self.after(current)

    # O(1)
    def __len__(self):
        return self._number_of_items

    # O(1)
    def add_last(self, data):
        # last item's next will be the dummy node
        return self._make_position( \
            self._add_between(data, next_node=self._dummy_node, previous_node=self._dummy_node.previous))

    # O(1)
    def add_first(self, data):
        return self._make_position( \
            self._add_between(data, next_node=self._dummy_node.next, previous_node=self._dummy_node))

    # O(1)
    def delete(self, position):
        node = self._validate(position)
        # next_node = node.next
        # next_node.previous = node.previous
        node.next.previous = node.previous
        node.previous.next = node.next
        node.next = None # marks as invalid
        self._number_of_items -= 1
        return node.data