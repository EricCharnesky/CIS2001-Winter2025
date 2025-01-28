class ArrayBasedSequence:

    # O(1)
    def __init__(self):
        self._data = [None, None, None, None, None]
        self._number_of_items = 0

    # O(1)
    def __len__(self):
        return self._number_of_items

    # O(n)
    def _add_space(self):
        new_data = [ None ] * ( self._number_of_items * 2 )
        for index in range(self._number_of_items):
            new_data[index] = self._data[index]
        self._data = new_data

    # average O(1)
    def append(self, item):
        if self._number_of_items >= len(self._data):
            self._add_space()
        self._data[self._number_of_items] = item
        self._number_of_items += 1

    # O(n)
    def remove(self, item):
        for index in range(self._number_of_items):
            if self._data[index] == item:
                for index_to_shift in range(index+1, self._number_of_items):
                    self._data[index_to_shift-1] = self._data[index_to_shift]
                self._number_of_items -= 1
                break
        else:
            raise ValueError("item not found")

    # O(n)
    def find(self, item):
        for index in range(self._number_of_items):
            if self._data[index] == item:
                return index
        return -1

    # O(1)
    def __getitem__(self, index):
        self._check_for_valid_index(index)
        return self._data[index]

    def _check_for_valid_index(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("Invalid index")

    # O(1)
    def __setitem__(self, index, item):
        self._check_for_valid_index(index)
        old_item = self._data[index]
        self._data[index] = item
        return old_item