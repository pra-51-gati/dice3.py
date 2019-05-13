import random
def dice():
    num = random.randint(1,6)
    print(num)
    while(1):
       flag = str(input("Do you want to dice it up again:Enter 1 and if not enter    0"))
       if flag == '1':
         num = random.randint(1,6)
         print(num)
       else:
         print("ending the game")
         return

dice() 
