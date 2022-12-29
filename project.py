import random
number = random.randint(1,6)
# print(number)
i = 1
attempt = 0
while True:
    attempt+=1
    roll = int(input())
    if (number==roll):
        print("correct",",","your score", i)
        i += 1
    else:
        print("try again")
