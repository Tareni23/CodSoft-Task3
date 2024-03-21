def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

#to check if the board is full
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

#AI player
def evaluate(board):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    else:
        return 0

# Function for Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = float("-inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

#to make the AI move using Minimax algo
def ai_move(board):
    best_score = float("-inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

#to play the Tic-Tac-Toe game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row, col = ai_move(board)
            print("AI's move:")
            board[row][col] = "X"
        else:
            while True:
                try:
                    row = int(input("Enter row (1-3): ")) - 1
                    col = int(input("Enter column (1-3): ")) - 1
                    if board[row][col] == " ":
                        break
                    else:
                        print("That position is already taken. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            board[row][col] = "O"

        if check_win(board, "X"):
            print_board(board)
            print("AI wins!")
            break
        elif check_win(board, "O"):
            print_board(board)
            print("You win!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
      
play_game()
