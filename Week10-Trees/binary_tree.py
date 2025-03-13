class LinkedBinaryTree:


    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_children(self):
        if self.left:
            yield self.left
        if self.right:
            yield self.right


    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def add_left(self, data):
        if self.left:
            raise ValueError("Already have a left child")
        self.left = LinkedBinaryTree(data, parent=self)

    def add_right(self, data):
        if self.right:
            raise ValueError("Already have a left child")
        self.right = LinkedBinaryTree(data, parent=self)


items_tree = LinkedBinaryTree("item")
items_tree.add_left("non taxable items")
items_tree.add_right("taxable items")

left_tree = items_tree.get_left()

left_tree.add_left("groceries")
left_tree.add_right("hygiene products")

right_tree = items_tree.get_right()
right_tree.add_left("items that we sell extended warranties for")
right_tree.add_right("cheap things you'll have to replace often")



