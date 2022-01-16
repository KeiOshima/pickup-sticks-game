#loo to make sure player doesnt get to play game until proper answer is given. 
print("Hello welcome to the pick-up sticks game!! The rules are quite simple ")
print("At the start of the game both players will decide on how mny sticks they want ot play with")
print("The minimum number of sticks required to play is 10")
print("if you want a longer game chhose to play with more sticks")
print("each player will take turn picing up 1-3 sticks.")
print("the winner of the gam is the player to not pick up the last sticks.")
player_one_point = 0
player_two_point = 0
game =True;
while game == True:
    sticks = int(input("how many sticks to start (minimum 10): "))
    while sticks < 10:
        if sticks < 10:
            print("sorry, thats too few sticks try again.")
            sticks = int(input("how many sticks to start (minimum 10):"))
    print("great, let's play!!!")
    print()
    #set varaible for players turn
    y = 0
#a loop within a loop in order to make it two player and to play until there are no more sticks
    while sticks > 0:
        while y == 0 :
            print("Player 1 turn:")
            print("there are",sticks," sticks on the table")
            x = int(input("how many sticks do you want to take (1,2 or 3):"))
            while x > 3 or x < 0 or x == 0:
                print("Sorry that's not a valid number of sticks pleaase try again")
                print()
                print("Player 1 turn:")
                print("there are",sticks,"sticks on the table")
                x = int(input("how many sticks do you want to take (1,2 or 3):"))
            #loop to make sure player gives correct input when theres less than 3 stikcs 
            while sticks < 3 and x > 2 or x==0:
                print("Sorry that's not a valid number of sticks pleaase try again")
                print()
                print("Player 1 turn:")
                print("there are",sticks,"sticks on the table")
                x = int(input("how many sticks do you want to take (1,2 or 3):"))
            #loop to make sure player gives correct answer when less than 2 sticks 
            while sticks < 2 and x > 1 or x==0:
                print("Sorry that's not a valid number of sticks pleaase try again")
                print()
                print("Player 1 turn:")
                print("there are",sticks,"sticks on the table")
                x = int(input("how many sticks do you want to take (1,2 or 3)?"))
            print("Player 1 picked up:",x,"sticks")
            sticks -= x
            #add + 1 to variable for player in order to switch to player 2
            y += 1
        if sticks == 0:
            break
        #now its player 2 
        while y == 1:
            print()
            print("Player 2 turn:")
            print("there are",sticks,"on the table")
            x = int(input("how many sticks do you want to take (1,2 or 3):"))
            while x > 3 or x < 0 or x == 0:
                print("Sorry that's not a valid number of sticks please try again")
                print()
                print("Player 2 turn:")
                print("there are",sticks,"sticks on the table")
                x = int(input("how many sticks do you want to take (1,2 or 3):"))
            while sticks < 3 and x > 2:
                print("Sorry that's not a valid number of sticks please try again")
                print()
                print("Player 2 turn:")
                print("there are",sticks,"sticks on the table")
                x = int(input("how many sticks do you want to take (1,2 or 3):"))
            while sticks < 2 and x > 1:
                print("Sorry that's not a valid number of sticks please try again")
                print()
                print("Player 2 turn:")
                print("there are",sticks,"sticks on the table")
                x = int(input("how many sticks do you want to take (1,2 or 3):"))
            print("Player 2 picked up:",x,"sticks")
            print()
            sticks -= x
            y -= 1
        if sticks == 0:
            break
    print("there are no sticks left in the game")
    if y == 0:
        print()
        print("player one wins")
        player_one_point += 1
        Choice = input("do you want to play again (yes/no):")
        if Choice == "no":
            game = False
            print("ScoreBoard:")
            print()
            print("player one win count:" + player_one_point)
            print("player two win count:" + player_two_point)
            print("thanks for playing!!")
        
    if y == 1:
        print()
        print("player two wins")
        player_two_point += 1
        Choice = input("do you want to play again (yes/no):")
        if Choice == "no":
            game = False
            print("ScoreBoard:")
            print()
            print("player one win count:",player_one_point)
            print("player two win count:",player_two_point)
            print("thanks for playing!!")
    
   
   
