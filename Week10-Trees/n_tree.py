from collections import deque

class Tree:

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        self.children.append(Tree(data))

    def is_leaf(self):
        return len(self.children) == 0

    def print_tree_depth_first(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

    def print_tree_breadth_first(self):
        items = deque()
        items.append(self)

        while len(items) != 0:
            current_tree = items.popleft()
            print(current_tree.data)
            for child in current_tree.children:
                items.append(child)
