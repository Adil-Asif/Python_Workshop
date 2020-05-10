import random

move = ["Rock","Paper","Scissor"] 



play = True
Tie = Win = Loss = 0

while play == True:
    
    computer = random.choice(move) #computer makes the move
    inp =False
    while True:
      
      user = input("Enter your move: ") #user enters the move
      user = user.upper()
      
      
      if (user == 'ROCK') or (user == 'PAPER') or (user == 'SCISSOR'):
          break
    
    computer = computer.upper()
    print(f"Computer's move {computer}")

    #Different possibilities for win or loss
    if user == computer:
        Tie+=1
    elif (user == "ROCK" and computer == "PAPER") or (user == "SCISSOR" and computer == "ROCK") or (user == "PAPER" and computer == "SCISSOR"):
        Loss+=1
    else:
        Win+=1
    
    print("1) Do you want to continue\n2) DO you want to exit") 
    n = input("Enter your choice: ")
 
    #checks to see if user want to finish the game
    if int(n) == 1:
        play = True
    else:
        play = False    

print(f"Games Won: {Win}\nGames Lost: {Loss}\nGames Tied: {Tie}\nGame Ended")