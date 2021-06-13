import random

inzet = random.randint (1,36)

def roulette():
    chips = 10
    begin = "Je hebt " + str(chips)+" chips!"
    print(begin)

    while True:
        inzetten = input("Op welke nummers wil je inzetten? ")
        if chips <= 0:
            print("GAME OVER")
        if inzetten == "STOP":
            break
        if int(inzet) <= 36 and int(inzet) >= 0:
            chips -= 1
        else:
            print("Invalid input")
        if chips == 0:
            print("rien ne va plus")


    if inzetten == "STOP":
        print("rien ne va plus")
        print("De uitkomst is " + str(chips))

    if inzet | inzet:
        chips = chips + 35
    else:
        chips -= 1

    print("Je hebt nog " + str(chips) + " chips!")
roulette()
