
# UMGPT : prompt - write a binary search tree class in python

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursively(self.root, result)
        return result

    def _in_order_traversal_recursively(self, node, result):
        if node is not None:
            self._in_order_traversal_recursively(node.left, result)
            result.append(node.key)
            self._in_order_traversal_recursively(node.right, result)


    # UMGPT Prompt: add a remove function

    def remove(self, key):
        self.root = self._remove_recursively(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _remove_recursively(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove_recursively(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursively(node.right, key)
        else:
            # Node with key found
            # Case 1: Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 2: Node with two children
            # Get the in-order successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)

            # Copy the successor's content to this node
            node.key = successor.key

            # Delete the successor
            node.right = self._remove_recursively(node.right, successor.key)

        return node



# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(20)
bst.insert(12)

print(bst.search(5))  # Output: True
print(bst.search(20))  # Output: False
print(bst.in_order_traversal())  # Output: [5, 10, 15]

bst.remove(5)

print(bst.in_order_traversal())


def _check_bst_node(some_node):
    if some_node is None:
        return True
    if (some_node.left is not None
        and some_node.left.key > some_node.key) \
            or (some_node.right is not None
                and some_node.right.key < some_node.key):
        return False
    return _check_bst_node(some_node.left) and _check_bst_node(some_node.right)

def check_bst_bad(some_tree):
    return _check_bst_node(some_tree.root)

def _check_bst_in_order(some_node, keys):
    if some_node is None:
        return
    _check_bst_in_order(some_node.left, keys)
    keys.append(some_node.key)
    _check_bst_in_order(some_node.right, keys)

def check_bst_in_order(some_tree):
    keys = []
    _check_bst_in_order(some_tree.root,  keys)
    for index in range(1, len(keys)):
        if keys[index] < keys[index-1]:
            return False
    return True


print(check_bst_bad(bst))

bst.root.right.left.key = 8

print(check_bst_bad(bst))
print(check_bst_in_order(bst))