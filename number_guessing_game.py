import random

number = random.randint(1, 10)  # random number between 1 and 10


i=1
while i<=5:
    guess=int(input("ENTER THE NUMBER FOR GUSSING bet(1-10)= "))
    if number == guess:
        print("CONGRATULATION!YOU CORRECTLY GUESS THE NUMBER")
        break
    else:
        print("Wrong Guess Attempt left :",5-i)    
    i+=1
else:
     print("Game over correct number was",number)   
