from random import randint
for i in range(0,100):
    number = randint(1,4)
    if number != 4:
        print(i,number)
    else:
        while number == 4:
            number = randint(1,4)
        print(i,number)
