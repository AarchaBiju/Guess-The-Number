import random 
n = random.randint(0,9)
print(n)
print("Guess a number between 1 to 9")
chances=0

while(chances< 5):
    guess = int(input("Enter your guess"))
    if(n == guess):
        print("The guess was correct")
        break
    elif guess<n:
        print(" Your guessed number is low, think a higher number ", guess)
    else :
        print(" Your guessed number is high, think a lower number ", guess)   
chances+=1   