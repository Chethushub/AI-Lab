import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def try_win_or_block(board, player):
    """
    Check all empty cells and see if placing 'player' there wins the game.
    Return the winning cell if exists, else None.
    """
    for (r, c) in get_empty_cells(board):
        board[r][c] = player
        if check_winner(board, player):
            board[r][c] = ' '  # Undo move
            return (r, c)
        board[r][c] = ' '  # Undo move
    return None

def sys_move(board, sys_player, human_player):
    # 1. Try to win
    win_move = try_win_or_block(board, sys_player)
    if win_move:
        return win_move

    # 2. Try to block human's win
    block_move = try_win_or_block(board, human_player)
    if block_move:
        return block_move

    # 3. Otherwise, random move
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    sys_player = 'O'

    while True:
        print_board(board)

        # Human turn
        print("Your turn (X):")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Choose from 0, 1, or 2.")
            continue

        if board[row][col] != ' ':
            print("Spot taken! Choose another.")
            continue

        board[row][col] = human_player

        if check_winner(board, human_player):
            print_board(board)
            print("You win! 🎉")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # System turn
        print("System's turn (O):")
        move = sys_move(board, sys_player, human_player)
        if move:
            board[move[0]][move[1]] = sys_player
            if check_winner(board, sys_player):
                print_board(board)
                print("System wins! 😢")
                break
        else:
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
