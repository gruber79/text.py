print("Play the Game")
roll = int(input("How many rolls are you want to play: "))
money = int(input("How much money you want to put: "))
num = int(input("choose the winning number, 1 to 10: "))
import random
win = random.randint(1, 10)
print(win)
a = money / roll
for x in range(roll):
  if num == win:
    b = (a * roll) * 2
    print("You Win "+ str(b)+" " + "dolar")
    price = str(input("do you want to continue "))
    if price == "no":
      break
    else:
      newprice = int(input("How much you want to play: ")) 
      a = newprice / roll 
  else: 
    roll = roll - 1
    print("You have "+ str(roll) + " chance to play")  
    if roll == 0:
      print("YOU LOSE ALL YOUR MONEY ")
      price = str(input("do you want to continue "))
      money = int(input("How much money you want to put: "))
      roll = int(input("How many rolls are you want to play: "))
    ask = str(input("You want to continue. "))
    if ask == "yes":
      num = int(input("choose the winning number, 1 to 10: ") )

    