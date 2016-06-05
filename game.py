from random import randint
board=[]
score=0
for x in range(5):
    board.append(["O"]*5)
def print_board(board):
    for row in board:
        print" ".join(row)
print "Your Ground"        
print_board(board)
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
for turn in range(4):

    play =raw_input('Play? (y/n)')
    if (play == "y" or play =="Y"):
        target_row = random_row(board)
        target_col = random_col(board)
    
        print "Lets Play"
        if(target_row < 0 or target_row > 4) or (target_col < 0 or target_col > 4):
            print "Oops!..You missed."
        else:
            board[target_row][target_col]= "X"
            print_board(board)
            if (target_row == 0 or target_row == 4) or (target_col == 0 or target_col == 4):
                score =score+10
            elif (target_row == 1 or target_row == 3) or (target_col == 1 or target_col == 3):
                score =score+30
            elif (target_row == 2 and target_row == 2):
                score =score+50 
   	    print "*****************"
            print "*Your score:",score,"*"
	    print "*****************"	
    elif (play == "n" or play =='N'):
        print "See u later."
        break
    else:
        play=print("Sorry, I didn't catch that.")
	
    turn=turn+1
    if turn==4:
        print "Game Over"


