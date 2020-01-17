print("Enter the size for the chessboard")
size = input("-~-~-~> ");
board = "";
if size.isdigit():
    int_size = int(size)
    for y in range(0 ,int_size):
        for x in range(0, int_size):
            if (x + y) % 2 == 0:
                board += " "
            else:
                board += "#"
        board += "\n";
else:
    print("Sorry, that cannot make a valid grid!")
print(board)
