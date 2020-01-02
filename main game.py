#title card not found
#god help me piece this together please

board1 = [" "," "," "," "," "," "," "," "," "," "]
aTuple = (1,2,3,4,5,6,7,8,9)
player1 = []
player2 = []

'''board = 7,8,9,
           4,5,6,
           1,2,3'''

def playerTurn(y,x):
    
    if x % 2 !=0:
        player1.append(y)
        board1[y] = "X"
            
    elif x % 2 ==0:    
        player2.append(y)
        board1[y] = "O"

def gameGrid():
    print(str(board1[7]) , " | " , str(board1[8]), " | " , str(board1[9]))
    print("")
    print(str(board1[4]) , " | " , str(board1[5]) , " | " , str(board1[6]))
    print("")
    print(str(board1[1]) , " | " , str(board1[2]) , " | " , str(board1[3]))


def winO(y):
    global aTuple, player2
    '''Winner set for PLayer O'''
    if set(aTuple).intersection(player2) == {1,2,3}:
       return "0"
    elif set(aTuple).intersection(player2) == {4,5,6}:
        return "0"   
    elif set(aTuple).intersection(player2) == {7,8,9}:
        return "0"
    elif set(aTuple).intersection(player2) == {1,4,7}:
        return "0"
    elif set(aTuple).intersection(player2) == {2,5,8}:
        return "0"
    elif set(aTuple).intersection(player2) == {3,6,9}:
        return "0"
    elif set(aTuple).intersection(player2) == {1,5,9}:
        return "0"
    elif set(aTuple).intersection(player2) == {3,5,7}:
        return "0"
    else:
        pass
       
def winX(y):
    global aTuple, player1
    '''Winner set for PLayer X'''
    if set(aTuple).intersection(player1) == {1,2,3}:
       return "1"
    elif set(aTuple).intersection(player1) == {4,5,6}:
        return "1"
    elif set(aTuple).intersection(player1) == {7,8,9}:
        return "1"
    elif set(aTuple).intersection(player1) == {1,4,7}:
        return "1"
    elif set(aTuple).intersection(player1) == {2,5,8}:
        return "1"
    elif set(aTuple).intersection(player1) == {3,6,9}:
        return "1"
    elif set(aTuple).intersection(player1) == {1,5,9}:
        return "1"
    elif set(aTuple).intersection(player1) == {3,5,7}:
        return "1"
    else:
        pass
       

def greetingStart():
    print("Hello Players! Welcome to TikTokToe!")

def endScreen():
    try:
        ending = input("Thanks for Playing!\n See you next Time!")
    except ValueError:
        raise ValueError
        exit() 
    else:
        exit() #figure out a "new game" mechanic

turn1 = 1
def gameRun():
    global turn1, board1

    while turn1 <= 9:

        if turn1 == 1:
            greetingStart()
            gameGrid()
        if turn1 % 2 != 0:
            print("Player 1! Your Turn!\n")
        elif turn1 % 2 == 0:
            print("Player 2! Your Turn!\n")
        try:
            y = int(input("Enter a Number: "))
        except ValueError:
            continue
        else:
            if  y > 9 or y < 1:
                continue
            if y == "exit":
                break
            playerTurn(y,turn1)
            gameGrid()
            turn1 += 1
            winO(y)
            if winO(y) == "0":
                print("Player2 Wins")
                break
            winX(y)
            if winX(y) == "1":
                print("Player1 Wins")
                break
            if turn1 == 9:
                print("DRAW")
    
    
            
gameRun()
