board = []

for i in range(9):
    board.append(input("Enter 9 numbers for row "+str(i+1)+": "))
def sudokuCheck(board):
    SET_OF_NINE = set((1,2,3,4,5,6,7,8,9))

    #checks rows
    for row in board:
        comparisonSet = set(())
        for ch in row:
            comparisonSet.add(int(ch))
        if comparisonSet != SET_OF_NINE:
            return False

    #checks columns
    for col in range(9):
        comparisonSet = set(())
        for row in board:
            comparisonSet.add(int(row[col]))
        if comparisonSet != SET_OF_NINE:
            return False
    
    #checks 3x3 tiles
    for j in range(0,7,3):
        for k in range(0,7,3):
            comparisonSet = set(())
            for row in range(0 + j, 3 + j):
                for col in range(0 + k, 3 + k):
                    comparisonSet.add(int(board[row][col]))
            if comparisonSet != SET_OF_NINE:
                return False
    return True

if(sudokuCheck(board)):
    print("Yes")
else:
    print("No")

