import random
guess=random.randint(0,100)
a=0
for i in range(0,3):
    user=int(input("enter the number you think will get randomly from 0 to 99: "))
    if user==guess:
        a=1
        print("Hurray!!! you guess the right number..")
        break
    else:
        print("Try Again!! you can do it")

if a==0:
    print("Better luck next time and the number you need to guess is ", guess)
