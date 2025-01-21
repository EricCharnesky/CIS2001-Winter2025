class NQueens:

    QUEEN = 'Q'
    OPEN = ' '

    def __init__(self):
        self.board = []
        for row in range(8):
            self.board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.number_of_queens = 0

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    def _is_column_open(self, column_index):
        for row_index in range(self.number_of_queens):
            if self.board[row_index][column_index] == self.QUEEN:
                return False
        return True

    def _is_backwards_diagonal_open(self, row_index, column_index):
        while row_index > 0 and column_index > 0:
            if self.board[row_index][column_index] == self.QUEEN:
                return False
            row_index -= 1
            column_index -= 1
        return True

    def _is_forwards_diagonal_open(self, row_index, column_index):
        while row_index > 0 and column_index < 8:
            if self.board[row_index][column_index] == self.QUEEN:
                return False
            row_index -= 1
            column_index += 1
        return True


    def _can_place(self, column_index):
        return self._is_column_open(column_index) \
            and self._is_backwards_diagonal_open(self.number_of_queens, column_index) \
            and self._is_forwards_diagonal_open(self.number_of_queens, column_index)

    def solve(self):
        # print(self)
        # print()
        # base case
        if self.number_of_queens == 8:
            print(self)
            print()
        else:
            for column_index in range(8):
                if self._can_place(column_index):
                    self.board[self.number_of_queens][column_index] = self.QUEEN
                    self.number_of_queens += 1
                    self.solve()
                    self.number_of_queens -= 1
                    self.board[self.number_of_queens][column_index] = self.OPEN