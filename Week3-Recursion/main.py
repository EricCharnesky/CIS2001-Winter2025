from maze_solver import MazeSolver
from n_queens import  NQueens

def bad_fib(nth):
    # base case - simple solution
    if nth <= 1:
        return 1
    # break down a complex problem - approach the base case
    return bad_fib(nth-1) + bad_fib(nth-2)

def iterative_fib(nth):
    current_nth = 0
    previous = 0
    current = 1

    while current_nth != nth:
        next = current + previous
        previous = current
        current = next
        current_nth += 1
    return current

for number in range(50):
    print(f'{number}: {iterative_fib(number)}')

maze = [
    ['S', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' '],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', 'E'],
    ['X', 'X', ' ', ' ', ' ']
]

maze_solver = MazeSolver(maze)

maze_solver.solve()

n_queens = NQueens()
n_queens.solve()