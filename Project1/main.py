from wsgiref.simple_server import software_version


class CheckersSolver:

    BOARD_SIZE = 8
    EMPTY = " "
    BLACK = 'B'
    WHITE = 'W'

    def __init__(self, board):
        if len(board) != self.BOARD_SIZE and any(len(row) != self.BOARD_SIZE for row in board):
            raise ValueError("invalid board size")

        pieces_on_even = None
        for row_index in range(self.BOARD_SIZE):
            for column_index in range(self.BOARD_SIZE):
                if board[row_index][column_index] != self.EMPTY:
                    if pieces_on_even is None:
                        pieces_on_even = row_index + column_index % 2 == 0
                    else:
                        if pieces_on_even != ( row_index + column_index % 2 == 0 ):
                            raise ValueError("Pieces on more than 1 color")

        self._board = board
        self._current_jumps = 0
        self._max_jumps = 0

    # https://github.com/EricCharnesky/CIS2001-Winter2025/blob/main/Lab3/main.py
    def __str__(self):
        return "\n".join(str(row) for row in self._board)

    def _can_jump_to(self, start_row_index, start_column_index, target_row_index, target_column_index):
        return 0 <= target_row_index < self.BOARD_SIZE and 0 <= target_column_index < self.BOARD_SIZE \
            and self._board[target_row_index][target_column_index] == self.EMPTY \
            and self._board[(start_row_index + target_row_index) // 2][(start_column_index + target_column_index) // 2] == self.BLACK

    def get_max_jumps(self):
        for row_index in range(self.BOARD_SIZE):
            for column_index in range(self.BOARD_SIZE):
                if self._board[row_index][column_index] == self.WHITE:
                    self._get_max_jumps(row_index, column_index)
        return self._max_jumps

    def _get_max_jumps(self, row_index, column_index):
        self._max_jumps = max(self._current_jumps, self._max_jumps)

        moves = ( (-2, -2), (-2, 2), (2, -2), (2, 2) )

        for move in moves:
            target_row_index = row_index+move[0]
            target_column_index =  column_index+move[1]
            if self._can_jump_to(row_index, column_index, target_row_index, target_column_index):
                piece = self._board[row_index][column_index]
                jumped_piece = self._board[row_index + move[0] // 2][column_index + move[1] // 2]

                self._current_jumps += 1
                self._board[target_row_index][target_column_index] = piece
                self._board[row_index+move[0]//2][column_index+move[1]//2] = self.EMPTY
                self._board[row_index][column_index] = self.EMPTY
                self._get_max_jumps(target_row_index, target_column_index)
                self._board[row_index][column_index] = piece
                self._board[row_index + move[0] // 2][column_index + move[1] // 2] = jumped_piece
                self._board[target_row_index][target_column_index] = self.EMPTY
                self._current_jumps -= 1

        return self._max_jumps



board = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
[' ', ' ', 'W', ' ', 'W', ' ', ' ', ' '],
[' ', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', 'B', ' ', ' ', ' ', 'B'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

solver = CheckersSolver(board)

print(solver.get_max_jumps())