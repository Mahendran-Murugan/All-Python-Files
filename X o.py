board = ["" for x in range(9)]


def print_board():
    row1 = '|{}||{}||{}|'.format(board[0], board[1], board[2])
    row2 = '|{}||{}||{}|'.format(board[3], board[4], board[5])
    row3 = '|{}||{}||{}|'.format(board[6], board[7], board[8])
    print("\n" + row1 + "\n" + row2 + "\n" + row3 + '\n')


def move(ic):
    if ic == 'X':
        number = 1
    elif ic == 'O':
        number = 2
    print("Your turn {}".format(number))
    choice = int(input("Enter your move(1-9):").strip().upper())
    if board[choice - 1] == "":
        board[choice - 1] = ic
    else:
        print()
        print("That place is taken!!!")


def win(ic):
    if (board[0] == ic and board[1] == ic and board[2] == ic) \
            or (board[3] == ic and board[4] == ic and board[5] == ic) \
            or (board[6] == ic and board[7] == ic and board[8] == ic) \
            or (board[0] == ic and board[3] == ic and board[6] == ic) \
            or (board[1] == ic and board[4] == ic and board[7] == ic) \
            or (board[2] == ic and board[5] == ic and board[8] == ic) \
            or (board[0] == ic and board[4] == ic and board[8] == ic) \
            or (board[6] == ic and board[4] == ic and board[2] == ic):
        return True
    else:
        return False


def draw():
    if "" not in board:
        return True
    else:
        return False


while True:
    print_board()
    move("X")
    print_board()
    if win("X"):
        print("Player 1 Won!!")
        break
    elif draw():
        print('Draw')
        break
    move("O")
    print_board()
    if win("O"):
        print("Player 1 Won!!")
        break
    elif draw():
        print("Draw")
        break
