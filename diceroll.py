import random 
while True:     
     print(" 1. roll the dice")
     print(" 2. Exit")    
     user = int(input("what you want to do\n"))     
     if user==1:         
        number = random.randint(1,6)         
        print(number)     
     else:       
        break