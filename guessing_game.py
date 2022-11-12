#!/usr/bin/env python
import random
minimum= int(input("Enter Lower bound: "))
maximum= int(input("Enter Upper bound: "))
answer=random.randint(minimum,maximum)
print(answer)
guess=input("enter a number: " )
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
