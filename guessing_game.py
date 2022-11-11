#!/usr/bin/env python
import random
minimum=1
maximum=20
answer=random.randint(minimum,maximum)
print(answer)
guess=input("enter a number between 1 and 20: " )
guess=int(guess)
while answer!= guess:
    if guess < answer:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > answer:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")
