def display_table():
    #convert the table into readable tictactoe, 0 = whitespace,1 = O and 2 = X
    global r1,r2,r3
    l1,l2,l3 = [],[],[] #lists to be printed
    selected_printcandidate = 0

    for row in [r1,r2,r3]:

        if row is r1:
                selected_printcandidate = l1
        elif row is r2:
            selected_printcandidate = l2
        else:
            selected_printcandidate = l3

        for i in row:

            if i == 0:
                selected_printcandidate.append(" ")
            elif i == 1:
                selected_printcandidate.append("O")
            else:
                selected_printcandidate.append("X")            
    
    print(l1)
    print(l2)
    print(l3)
    print("")
    print("""Enter using keypad keys 1-9
       7 8 9
       4 5 6
       1 2 3""") 
            
def can_fill(n): #n is a keypad key
    #finish later
    if n < 4:
        if r3[n-1] != 0:
            return False
    elif n < 7:
        if r2[n-4] != 0:
            return False
    elif n < 10:
        if r1[n-7] != 0:
            return False
    return True


def table_insert(n,current_player_symbol):
    ###used to convert n into player choice and insert it into the table. does not validate input (n)
    global r1,r2,r3
    

    ##index conversion
    #n-1 for r3
    #n-4 for r2
    #n-7 for r1

    if n < 4:  #r3, 1,2,3
        r3[n - 1] = current_player_symbol

    elif n < 7: #r2 1,5,6
        r2[n - 4] = current_player_symbol
    else:
        r1[n - 7] = current_player_symbol


def gameover(): #return false if no and encoded list
                #result[player,position] if yes 
    global r1,r2,r3

    #is it a draw yet?
    draw = True
    for row in [r1,r2,r3]:
        for i in row:
            if i == 0:
                draw = False
    if draw == True:
        return ["D",""]
    
    #row check
    for row in [r1,r2,r3]: #if all are same and not 0
        if row[0] == row[1] and row[1] == row[2] and row[2] != 0: 
             if row[0] == 1:
                return ["O",row]    #row is list         
             else:
                return ["X",row]
    
    #column check
    for i in range(0,3):
        if r1[i] == r2[i] and r2[i] == r3[i] and r3[i] != 0:
            if r1[i] == 1:
                return ["O",i]#i is a number, so check for int
                              #when function is called
            else:
                return ["X",i]

    #diagonal check
    if r3[0] == r2[1] and r2[1] == r1[2] and r1[2] != 0:
        if r1[2] == 1:
            return ["O","1-9"] #check for string on the other side
        else:
            return ["X","1-9"]

    if r1[0] == r2[1] and r2[1] == r3[2] and r3[2] != 0:
        if r3[2] == 1:
            return ["O","7-3"]#check for string when function is called
        else:
            return ["X","7-3"]

    return False
r1 = [0,0,0]  #7 8 9
r2 = [0,0,0]  #4 5 6
r3 = [0,0,0]  #1 2 3
# 1 = 0,2 = x
#keypad representative

#redundant code, here for future implementations of player vs computer
#currently PvP, X first
while True:

    pl1 = input("PLAYER_ONE: Enter 1 to play as O or 2 to play as X\n")
    if pl1 == "1" or pl1 == "2": #check if only number entered & convert to int type if so
        pass
    else:
        continue

    pl1 = int(pl1)

    if pl1 == 1:  #pl2 is other symbol
        pl2 = 2
        break
    elif pl1 == 2:
        pl2 = 1
        break

current_player = 2  #X gets to go first
valid_keys = [] 
for m in range(1,10):
    valid_keys.append(str(m))
while True:
    
    display_table()
    if gameover() != False:#is it a draw or win for someone?
        print("\n")
        result = gameover()
        winner = result[0]
        if winner == "D":
            print("IT'S A TIE")
            break
        else:
            print(f"{winner} WINS!")
            break

    #print who's playing now
    if current_player == 1:
        current_symbol = "O"
    else:
        current_symbol = "X"
    print(f"TURN OF {current_symbol}:\n ")

    a = input("     ")

    #check if given input is correct and can be used
    if a not in valid_keys: #if a is not a string between 1-9
        print("Enter only given numbers.\n")
        continue
    else:
        if can_fill(int(a)) == False:  # if a's positon is already occupied
            print(f"Position {a} is already occupied")
            continue
    table_insert(int(a), current_player)
    


    if current_player == 1: #switch turns at the end of each gameloop
        current_player = 2
    else:
        current_player = 1