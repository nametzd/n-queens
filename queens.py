# Daniel Nametz
# 8x8 queens board
# 9/25/19

import random

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j] == i:
                if j != len(board)-1:
                    print(" 1 ", end = '')
                else: 
                    print(" 1 ")
            else: 
                if j != len(board)-1:
                    print(" 0 ", end = '')
                else:
                    print(" 0 ")

#
# function checks the fitness level of the given board of queens
# if a queen is attacking another queen then a point gets added to the fitness counter
# the higher the fitness counter, the worse the fitness
# 
def checkQueens(state):
    fitnessCounter = 0
    for i in range(len(state)):
        for j in range(i+1,8):
            if(state[i]==state[j]):         # same row
                fitnessCounter+=1
            elif(state[i]-j+i==state[j]):   # checks upward diagonal
                fitnessCounter+=1
            elif(state[i]+j-i==state[j]):   # checks downward diagonal
                fitnessCounter+=1   
    #print("Count: ", fitnessCounter)        # displays fitness counter
    return fitnessCounter

#
# local k-beam search detects whether you reached goal of no attacking queens
# returns true or false
#
def localBeam(k):
    success = False
    fringe = []
    counter = 0
    # first generation is created
    while counter < k:
        queens = []
        for _ in range(0,8):
            queens.append(random.randrange(8))
        
        entry = [checkQueens(queens), queens]
        fringe.append(entry)
        fringe.sort()
        
        print("Fringe: ", fringe)

        counter+=1
        
    counter = 0
    iterations = 0
    
    while iterations < 100:
        while counter < k:
            copy = fringe[counter][1][:] # copy equals the board layout
            # in each iteration, all successors of all k states are generated. 

            # pick queen(0,7) in fringe to change 
            changeQueen = random.randint(0,7)

            # pick what to change it to (0,7)
            while True:
                newNum = random.randint(0,7)
                if newNum != copy[changeQueen]:
                    copy[changeQueen] = newNum
                    break

            # add new guy to fringe
            entry = [checkQueens(copy), copy]
            fringe.append(entry)
            counter+=1
        

        fringe.sort()
        # pops off all the worse nodes off of fringe
        while len(fringe) > k:
            fringe.pop(k)

        print("fringe: ", fringe)
        # if goal is met, stop
        if fringe[0][0] == 0:
            print("Complete! Board is: ", fringe[0][1])
            success = True
            printBoard(fringe[0][1])
            break

        counter = 0
        iterations+=1
    if success == False:
        print("Sorry! Board was not completed. Best board was: ", fringe[0])
        printBoard(fringe[0][1])



# main
#test = [2,4,0,7,1,2,3,3]
#checkQueens(test)
beamSize=5
localBeam(beamSize)

#print(queens)
#checkQueens(queens)