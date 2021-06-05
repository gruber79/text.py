print("Play the Dice Guessing Game") #Initial 

money = int(input("How much money you want to put: ")) ## Ask user for their bet
roll = int(input("How many rolls are you want to play: ")) # Ask user times to play
ram = roll
import random #import random function
userPoints=int(0)
computerPoints=int(0)

for x in range(roll): # for loop how many rolls user play
  
  win = random.randint(1, 6) #Defines win variable as a random integer in the range of 1 to 10
  num = int(input("choose the winning number, 1 to 6: ")) # Ask user for guess  
    
  if num == win: # if the num user choose is == to random number 
    print("You Win ") #Congratulating that you won.
    userPoints = int(userPoints) + 1#counting user's win.

  elif num is not win:
    computerPoints = int(computerPoints) + 1
    print("Your number is: "+ str(num))
    print("The dice roll is: "+ str(win))
    print("The House win")
        
  roll = roll - 1
  print("You have "+ str(roll) + " more chance to play") #it's show how many time the user has to play.
  print("         ")  
if  userPoints > computerPoints:
    money = money * 2
    print("You won " + str(userPoints) + " times out of " + str(ram))
    print("Your win: $" + str(money))
    
elif userPoints == computerPoints:
  print("Is a draw") 
  print("The house win")     
else:
  print("your lose all the money")

print("Thanks for playing have a wanderful day")

    
    
    
    
    
    
    
    
