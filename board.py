# Prints the board
def print_board(board):
    print("Printing board...")
    for i in board:
        print(i)


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

    print("\nPlayer", player_id, "added a mark at", "%d,%d" % (row_input, col_input))

    return board


def main():
    # Creates board
    board_top = ['-', '-', '-']
    board_mid = ['-', '-', '-']
    board_bot = ['-', '-', '-']
    board = [board_top, board_mid, board_bot]

    print("Printing board...")
    for i in board:
        print(i)

    win = False
    while not win:
        print("\nPlayer 1's turn!")
        row_input = int(input("Which row (0 - 2): "))
        col_input = int(input("Which column (0 - 2): "))
        player_id = 1
        place_mark(row_input, col_input, board, player_id)
        print_board(board)

        print("\nPlayer 2's turn!")
        row_input = int(input("Which row (0 - 2): "))
        col_input = int(input("Which column (0 - 2): "))
        player_id = 2
        place_mark(row_input, col_input, board, player_id)
        print_board(board)


main()
