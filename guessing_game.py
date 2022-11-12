#!/usr/bin/env python
import random
count=0
difficulty=input("Choose a difficulty (Easy, Medium, Hard, Hardcore): ")
if difficulty=="Easy":
   minimum=0
   maximum=10
elif difficulty=="Medium":
   minimum=0
   maximum=50
elif difficulty=="Hard":
   minimum=0
   maximum=100
elif difficulty=="Hardcore":
   minimum=0
   maximum=1000
else:
   print("enter difficulty again: ")
minimum= int(minimum)
maximum= int(maximum)
answer=random.randint(minimum,maximum)
print(answer)
guess=input("enter a number: " )
guess=int(guess)
while count >=0:
    count+=1
    if guess < answer:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > answer:
        print("Too high!")
        guess = int(input("Enter number again: "))
    elif guess == answer:
        print("you guessed it right!!")
        print(count)
        break
