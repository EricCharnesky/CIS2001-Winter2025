from glob import glob0


class MazeSolver:

    OPEN = " "
    BLOCKED = "X"
    START = 'S'
    END = 'E'
    VISITED = '.'

    def __init__(self, maze):
        self.maze = maze
        self.current_row_index = 0
        self.current_column_index = 0
        self.number_of_steps = 0
        for row_index in range(len(self.maze)):
            for column_index in range(len(self.maze[row_index])):
                if self.maze[row_index][column_index] == self.START:
                    self.current_row_index = row_index
                    self.current_column_index = column_index

    def _can_move_to(self, target_row_index, target_column_index):
        return 0 <= target_row_index < len(self.maze) and \
            0 <= target_column_index < len(self.maze[target_row_index]) and \
            ( self.maze[target_row_index][target_column_index] == self.OPEN or
              self.maze[target_row_index][target_column_index] == self.END )

    def _mark(self, mark):
        if self.maze[self.current_row_index][self.current_column_index] != self.START and \
                self.maze[self.current_row_index][self.current_column_index] != self.END:

            self.maze[self.current_row_index][self.current_column_index] = mark

    def __str__(self):
        return "\n".join(str(row) for row in self.maze)

    def solve(self):
        self._mark(self.VISITED)
        self.number_of_steps += 1
        #print(self)
        #print()
        # base case
        if self.maze[self.current_row_index][self.current_column_index] == self.END:
            print(self)
            print(f"solved in {self.number_of_steps} steps")
        # complex case
        else:
            # down
            if self._can_move_to(self.current_row_index+1, self.current_column_index):
                self.current_row_index += 1
                self.solve()
                self.current_row_index -= 1

            # right
            if self._can_move_to(self.current_row_index, self.current_column_index + 1):
                self.current_column_index += 1
                self.solve()
                self.current_column_index -= 1

            # left
            if self._can_move_to(self.current_row_index, self.current_column_index - 1):
                self.current_column_index -= 1
                self.solve()
                self.current_column_index += 1

            # up
            if self._can_move_to(self.current_row_index - 1, self.current_column_index):
                self.current_row_index -= 1
                self.solve()
                self.current_row_index += 1

        self._mark(self.OPEN)
        self.number_of_steps -= 1