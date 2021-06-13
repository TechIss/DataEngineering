operatie=input("Operatie?\n")
num1=float(input("Eerste getal?\n"))
num2=float(input("Tweede getal?\n"))
if operatie == "*":
    print("Resultaat: ", num1 * num2)
elif operatie == "+":
    print("Resultaat: ", num1 + num2)
elif operatie == "-":
    print("Resultaat: ", num1 - num2)
elif operatie == "/":
    if num2 == 0:
        print("Kan niet delen door 0")
    else:
        print("Resultaat:", num1 / num2)
else:
    print("Ongeldige Operatie")
