from os import system

board = [
            ["_","_","_","_","_","_"],
            ["_","_","_","_","_","_"],
            ["_","_","_","_","_","_"],
            ["_","_","_","_","_","_"],
            ["_","_","_","_","_","_"],
            ["_","_","_","_","_","_"]
          ]

selector = [" " for x in range(len(board[0]))]
selector[0] = "v"

def print_board():
    system("clear") # windows 'cls' mac 'clear'
    print(" ",  "_" * (len(board[0]) * 2 + 2))

    print(" ", "|", " ".join(x for x in selector), "|")

    for line in board:
        print(" ", "|", " ".join(str(x) for x in line), "|")

    print(" ","|" + "_" * (len(board[0]) *2 + 1) + "|" )

def move_selector(currIdx=0, flag=True):
    print_board()
    selector[currIdx] = " "
    entry = input()
    if entry == "r":
        if currIdx == len(board[0])-1:
            selector[currIdx]= "v"
        else:
            currIdx += 1
            selector[currIdx] = "v"
        move_selector(currIdx, flag)
    elif entry == "l":
        if currIdx == 0:
            selector[currIdx]= "v"
        else:
            currIdx -= 1
            selector[currIdx] = "v"
        move_selector(currIdx, flag)
    elif entry == "x":
        print("entry: ", entry)
        drop_piece(currIdx, flag)
    elif entry == "quit":
        return
    else:
        selector[currIdx] = "v"
        move_selector(currIdx, flag)
    return

def drop_piece(currIdx, flag):
    for i in range(1, len(board)+1):
        if board[0][currIdx] != "_":
            break
        if board[-i][currIdx] == "_":
            board[-i][currIdx] = "X" if flag else "O"
            flag = not flag
            break
    selector[currIdx] = "v"
    move_selector(currIdx, flag)
    return

move_selector()
