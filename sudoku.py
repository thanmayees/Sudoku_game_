def display_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid_move(board, row, col, num):
    # Check if num is already in the row
    if num in board[row]:
        return False

    # Check if num is already in the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if num is already in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def get_user_move():
    while True:
        try:
            row = int(input("Enter row (1-9): ")) - 1
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter number (1-9): "))
            if 0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9:
                return row, col, num
            else:
                print("Invalid input! Row and column must be between 1 and 9, and number must be between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def print_instructions():
    print("Welcome to Sudoku!")
    print("Fill in the missing numbers in the Sudoku grid.")
    print("Each row, column, and 3x3 subgrid must contain the numbers 1-9 without repetition.")
    print("Enter the row, column, and number (1-9) for each move.")
    print("Let's get started!\n")

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def main():
    print_instructions()

    # Example Sudoku board (0 represents empty cells)
    board = [
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

    print("Original Sudoku board:")
    display_board(board)

    while not is_board_full(board):
        row, col, num = get_user_move()
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            print("\nUpdated Sudoku board:")
            display_board(board)
        else:
            print("\nInvalid move! Please try again.")

    print("\nCongratulations! You solved the Sudoku puzzle.")

if __name__ == "__main__":
    main()
