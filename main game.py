'''TIKTOKTOE'''
#why does GITHUB SUCK SO MUCH SERIOUSLY GITHUB WHY

board1 = [" "," "," "," "," "," "," "," "," "," "]

player1 = []
player2 = []

'''board = 7,8,9,
           4,5,6,
           1,2,3'''

def playerTurn(y,x): #takes note of the player's turn
    
    if x % 2 !=0:
        player1.append(y)
        board1[y] = "X"
            
    elif x % 2 ==0:    
        player2.append(y)
        board1[y] = "O"

def gameGrid(): #visual representation of the game 
    print("\t" + str(board1[7]) , " | " , str(board1[8]), " | " , str(board1[9]))
    print("\t--------------")
    print("\t" + str(board1[4]) , " | " , str(board1[5]) , " | " , str(board1[6]))
    print("\t--------------")
    print("\t" + str(board1[1]) , " | " , str(board1[2]) , " | " , str(board1[3]))

def showGrid(): # grid to direct the player
    print("\t7" , " | " , "8" , " | " , "9")
    print("\t--------------")
    print("\t4" , " | " , "5" , " | " , "6")
    print("\t--------------")
    print("\t1" , " | " , "2" , " | " , "3")

def winGame(player): # win detection
    
    for x in player:
        if x == 1:  #all combinations that start with 1
            for x in player:
                if x == 2:
                    for x in player:
                        if x == 3:
                            return "1"
                if x == 4:
                    for x in player:
                        if x == 7:
                            return "1"
                if x == 5:
                    for x in player:
                        if x == 9:
                            return "1"
        if x == 2: #all combinations that start with 2
             for x in player:
                if x == 5:
                    for x in player:
                        if x == 8:
                            return "1"
        if x == 3: #all combinations that start with 3
            for x in player:
                if x == 6:
                    for x in player:
                        if x == 9:
                            return "1"
                if x == 5:
                    for x in player:
                        if x == 7:
                            return "1"
        if x == 4: # all combinations that start with 4:
            for x in player:
                if x == 5:
                    for x in player:
                        if x == 6:
                            return "1"
        if x == 7:
            for x in player:
                if x == 8:
                    for x in player:
                        if x == 9:
                            return "1"
        
    
def greetingStart():
    print("Hello Players! Welcome to TikTokToe!\nEnter a number from 1 to 9.\nEnter 0 to exit early.")
    
def endScreen(): #this is still shit fix it pls
    ending = input("Thanks for Playing!\n  Play Again? (Y/N): ").upper()
    if ending == "Y":
        resetGame(1)
        gameRun()
    elif ending == "N":
        print("See you next Time!")
        exit()
    else:
        print("Error")
        exit()

def resetGame(a): #fix this asap
    global name1, name2, player2, player1, board1, turn1
    board1 = [" "," "," "," "," "," "," "," "," "," "]
    player1 = []
    player2 = []
    name1 = ""
    name2 = ""
    turn1 = a

turn1 = 1
def gameRun(): #main game function
    global turn1, board1, player1, player2
    
    while turn1 <= 10:

        if turn1 == 1:
            greetingStart()
            showGrid()
            while turn1 == 1:
                name1 = input("Enter Your Name, Player 1!\n ")
                if name1 == " " or len(name1) > 15:
                    print("Enter your name within 15 characters.\n")
                    continue
                else:
                    name2 = input("Enter Your Name, Player 2!\n ")
                    if name2 == " " or len(name2) > 15:
                        print("Enter your name within 15 characters.\n")
                        continue
                    else:
                        break
        if turn1 % 2 != 0:
            print(name1 +  "! (X) Your Turn!\n")
        elif turn1 % 2 == 0:
            print(name2 +"! (O) Your Turn!\n")
        try:
            y = int(input("Enter a Number: "))
        except ValueError:
            continue
        else:
            if  y > 9 or y < -1:
                continue
            elif board1[y] != " ":
                print("\nPick another number")
                continue
            elif board1[y] != " ":
                print("\nPick another number")
                continue
            elif y == 0:
                endScreen()
            playerTurn(y,turn1)
            player1.sort()
            player2.sort()
            gameGrid()
            turn1 += 1
            winGame(player2)
            if winGame(player2) == "1":
                print("\n")
                print(name2 +" Wins!")
                winGame(player1)
            elif winGame(player1) == "1":
                print("\n")
                print(name1 +" Wins!")
            elif turn1 > 9:
                print("DRAW")
            elif turn1 > 9 or winGame(player1) == "1" or winGame(player2) == "1":
                endScreen()
            
gameRun()
