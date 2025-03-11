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

    def _print_tree_breadth_first(self, queue):
        pass # TODO - FINISH THURSDAY

    def print_tree_breadth_first(self):
        items = []
        items.append(self.data)
        for child in self.children:
            child._print_tree_breadth_first(items)

classification_system = Tree('Animalia')
classification_system.add_child('Chordata')
chordata = classification_system.children[0]

chordata.add_child("Mammalia")

mammalia = chordata.children[0]

mammalia.add_child('Diprotodontia')
mammalia.add_child('Primates')

diprotodontia = mammalia.children[0]
primates = mammalia.children[1]

diprotodontia.add_child('Quokka')
primates.add_child('Lemur')

classification_system.print_tree()





