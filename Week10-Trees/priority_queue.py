from binary_tree import LinkedBinaryTree

class MaxPriorityQueueList:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    # O(1)
    def get_max(self):
        return self.data[0]

    # O(1)
    def _get_left_child_index(self, index):
        left_child_index = index * 2 + 1
        if left_child_index >= len(self.data):
            return None
        return left_child_index

    # O(1)
    def _get_right_child_index(self, index):
        right_child_index = index * 2 + 2
        if right_child_index >= len(self.data):
            return None
        return right_child_index

    # O(log n)
    def _downheap(self, index):

        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)
        if left_child_index or right_child_index:
            largest_child_index = left_child_index
            if right_child_index and self.data[right_child_index] > self.data[left_child_index]:
                largest_child_index = right_child_index
            if self.data[index] < self.data[largest_child_index]:
                self._swap(index, largest_child_index)
                self._downheap(largest_child_index)

    # O(log n)
    def remove(self):
        data = self.data[0]

        item = self.data.pop()
        # when removing the last item, there is no index 0 to replace
        if len(self.data):
            self.data[0] = item

        self._downheap(0)

        return data

    # O(1)
    def _get_parent_index(self, index):
        return ( index - 1 ) // 2

    # O(log n)
    def _upheap(self, index):
        if index != 0:
            parent_index = self._get_parent_index(index)
            if self.data[index] > self.data[parent_index]:
                self._swap(index, parent_index)
                self._upheap(parent_index)

            #self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]

    # O(1)
    def _swap(self, index, parent_index):
        temp = self.data[index]
        self.data[index] = self.data[parent_index]
        self.data[parent_index] = temp

    # O (log n)
    def add(self, data):
        self.data.append(data)
        self._upheap(len(self.data)-1)


# throwaway
class MaxPriorityQueueLinked:

    def __init__(self, data):
        self.root = LinkedBinaryTree(data)

    def get_max(self):
        return self.root.data

    def remove_max(self):
        pass

    def _downheap(self, data, tree):
        if data > tree.data:
            if tree.left is None:
                tree.left = LinkedBinaryTree(tree.data, parent=tree)
                tree.data = data
                return
            if tree.right is None:
                tree.right = LinkedBinaryTree(tree.data, parent=tree)
                tree.data = data
                return
        else:
            if tree.left is None:
                tree.left = LinkedBinaryTree(data, tree)
                return
            if tree.right is None:
                tree.right = LinkedBinaryTree(data, tree)
                return

            return self._downheap(data, tree.left)




    def add(self, data):
        if self.root is None:
            self.root = LinkedBinaryTree(data)
        else:
            self._downheap(data, self.root)