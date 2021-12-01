import time


# Prints the board
def print_board(board):
    print("Printing board...")
    for i in board:
        print(i)


# Checks if a mark can be placed
def check_mark(row_input, col_input, board):
    mark_check = True
    board_top = board[0]
    board_mid = board[1]
    board_bot = board[2]

    # Checks if spot is out of the board
    if row_input < 0 or row_input > 2:
        print("Spot is out of the board, please try again.")
        mark_check = False
        return mark_check

    elif col_input < 0 or col_input > 2:
        print("Spot is out of the board, please try again.")
        mark_check = False
        return mark_check

    # Checks if spot is taken
    if row_input == 0:
        if board_top[col_input] == "X" or board_top[col_input] == "O":
            print("Spot already taken, please try again.")
            mark_check = False

    elif row_input == 1:
        if board_mid[col_input] == "X" or board_mid[col_input] == "O":
            print("Spot already taken, please try again.")
            mark_check = False

    elif row_input == 2:
        if board_bot[col_input] == "X" or board_bot[col_input] == "O":
            print("Spot already taken, please try again.")
            mark_check = False

    return mark_check


# Places a mark where the player has specified
def place_mark(row_input, col_input, board, player_id):
    board_top = board[0]
    board_mid = board[1]
    board_bot = board[2]

    # checks player id
    if player_id == 1:
        mark = "X"

    else:
        mark = "O"

    # Places mark
    if row_input == 0:
        board_top[col_input] = mark

    elif row_input == 1:
        board_mid[col_input] = mark

    elif row_input == 2:
        board_bot[col_input] = mark

    print("Player", player_id, "added a mark at", "%d,%d" % (row_input, col_input))

    return board


# Checks if the game has been won
def check_win(board, player_id):
    board_top = board[0]
    board_mid = board[1]
    board_bot = board[2]

    # Picks which mark to use
    if player_id == 1:
        mark = "X"

    else:
        mark = "O"

    # Checks all win scenarios
    return ((board_top[0] == mark and board_top[1] == mark and board_top[2] == mark) or  # across the top
            (board_mid[0] == mark and board_mid[1] == mark and board_mid[2] == mark) or  # across the middle
            (board_bot[0] == mark and board_bot[1] == mark and board_bot[2] == mark) or  # across the bottom
            (board_top[0] == mark and board_mid[0] == mark and board_bot[0] == mark) or  # down the left side
            (board_top[1] == mark and board_mid[1] == mark and board_bot[1] == mark) or  # down the middle
            (board_top[2] == mark and board_mid[2] == mark and board_bot[2] == mark) or  # down the right side
            (board_top[0] == mark and board_mid[1] == mark and board_bot[2] == mark) or  # diagonal
            (board_bot[0] == mark and board_mid[1] == mark and board_top[2] == mark))  # diagonal


def player_turn(board, player_id):
    # Asks for input
    print("\nPlayer %d's turn!" % player_id)
    row_input = input("Enter a row (0 - 2): ")
    col_input = input("Enter a column (0 - 2): ")
    print()

    # Makes sure input is a number
    while row_input.isdigit() is False or col_input.isdigit() is False:
        print("Please enter a number.")
        print_board(board)
        print("\nPlayer %d's turn!" % player_id)
        row_input = input("Enter a row (0 - 2): ")
        col_input = input("Enter a column (0 - 2): ")
        print()

    row_input = int(row_input)
    col_input = int(col_input)

    # Checks if the mark can be placed
    mark_check = check_mark(row_input, col_input, board)

    # Places the mark if possible
    if mark_check is True and player_id == 1:
        place_mark(row_input, col_input, board, player_id)

    elif mark_check is True and player_id == 2:
        place_mark(row_input, col_input, board, player_id)

    return mark_check


def main():
    # Creates board
    board_top = ['-', '-', '-']
    board_mid = ['-', '-', '-']
    board_bot = ['-', '-', '-']
    board = [board_top, board_mid, board_bot]
    elapsed_turns = 0

    print("Printing board...")
    for i in board:
        print(i)

    win = False
    while not win:
        # Player 1's turn
        player_id = 1
        while player_id == 1:
            mark_check = player_turn(board, player_id)
            win = check_win(board, player_id)
            print_board(board)

            # Ends game if won or a draw, otherwise makes sure player 1 has completed turn before switching turns
            if win is True:
                print("\nPlayer 1 wins!")
                time.sleep(5)
                exit(0)

            elif mark_check is False:
                player_id = 1

            elif elapsed_turns == 8:
                print("\nDraw game.")
                time.sleep(5)
                exit(0)

            elif mark_check is True:
                player_id = 2
                elapsed_turns += 1

        # Player 2's Turn
        while player_id == 2:
            mark_check = player_turn(board, player_id,)
            win = check_win(board, player_id)
            print_board(board)

            # Ends game if won, otherwise makes sure player 2 has completed turn before switching turns
            if win is True:
                print("\nPlayer 2 wins!")
                time.sleep(5)
                exit(0)

            elif mark_check is False:
                player_id = 2

            elif mark_check is True:
                player_id = 1
                elapsed_turns += 1


main()
