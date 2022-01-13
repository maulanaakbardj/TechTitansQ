from random import randint
value1 = randint(1,100)
value2 = randint(1,100)
#1 and 10 represent the range for your random value
print('Random Number 1 : '+str(value1))
print('Random Number 2 : '+str(value2))

if value1==value2:
    print('Result : Tie')
else :
    print('Result : No Tie')
