def is_valid(board, row, col, num):
    # Check if 'num' is not present in current row, current column, and current 3x3 grid
    return (
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[row//3*3 + i//3][col//3*3 + i%3] for i in range(9))
    )

def find_empty_location(board):
    # Find the first empty cell (cell with 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None  # If no empty cell is found

def solve_sudoku(board):
    row, col = find_empty_location(board)

    # If no empty cell is found, the puzzle is solved
    if row is None:
        return True

    # Try placing numbers 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the number didn't lead to a solution, backtrack
            board[row][col] = 0

    # If no number can be placed, backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_board(sudoku_board)
print("\nSolving...\n")

if solve_sudoku(sudoku_board):
    print("Sudoku Solution:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
