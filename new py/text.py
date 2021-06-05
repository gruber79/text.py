print("Play the Dice Guessing Game") #Initial 
roll = int(input("How many rolls are you want to play: ")) # Ask user times to play
money = int(input("How much money you want to put: ")) ## Ask user for their bet

import random #import random function
userPoints=int(0)
computerPoints=int(0)
a = money / roll # "a" gets the value of the money divided many times that user wants to play. 
for x in range(roll): # for loop how many rolls user play
    win = random.randint(1, 6) #Defines win variable as a random integer in the range of 1 to 10
    num = int(input("choose the winning number, 1 to 6: ")) # Ask user for guess  
    if num == win: # if the num user choose is == to random number 
        b = money * 2 #winnings multiplied by two
        print("You Win "+ str(b)+" " + "dolar") #Congratulating that you won with that amount of winnings.
        price = str(input("do you want to continue? ")) #Asking if you want to continue the game after winning.
        userPoints=int(userPoints)+1#counting user's win print
        money = b
        if price == "no": #Establishes condition for user input which ends the game
            print("Your win: $" + str(b)) #prints winning amount
            print("Thanks for playing") #congratulating
            break #system out
        else:
            print("you lose: $"+ str((a * roll) * 2))
            
    elif num is not win:
        computerPoints=int(computerPoints)+1
        print("The dice roll is: "+ str(win) + " your number is: "+ str(num)) 
        money=money-(a * money)
        print("you lose: $"+ str(money))
        price = str(input("do you want to continue? ")) #Asking if you want to continue the game after winning.
        if price == "no":
            print("Thank you for playing good luck next time.")
            break
    roll = roll - 1
    print("You have "+ str(roll) + " chance to play") #it's show how many time the user has to play.
    
if  userPoints > (roll/2):
    print("Your win: $" + str(money))
    
elif computerPoints == userPoints :
    print("Is a draw")
    
else:
    print("your lose all the money")
    
               

    
    
    
    
    
    
    
    
    
    '''    
if roll == 0:
   print("YOU LOSE ALL YOUR MONEY!") 
   ask = str(input("Do you want to continue? "))#Ask if the user wants to continue the game.
if ask == "yes": #If the user answers yes.
   num = int(input("choose the winning number, 1 to 10: ") ) #Ask the user to guess a number between 1-10.
if roll == 0:
   money = int(input("How much money you want to put: "))
   roll = int(input("How many rolls are you want to play: "))
'''   
   