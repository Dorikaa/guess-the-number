import random

number = random.randint(0,50)
print("In this game you have to guess a random generated number, good luck!")

cnt = 0

while cnt < 10:
    print("choose a number: ")
    alegere = input()
    alegere = int(alegere)

    cnt = cnt + 1

    if alegere < number:
        print("go higher: ")
    if alegere > number:
        print("go lower: ")

    if alegere == number:
        break

if alegere == number:
    cnt = str(cnt)
    print("gj, you found the number in ", cnt)

if alegere != number:
    number = str(number)
    print("you didnt find the number, it was: ", number)