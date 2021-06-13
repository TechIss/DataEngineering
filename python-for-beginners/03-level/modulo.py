
opera = input("Operatie? ")

a = input("Eerste getal? ")
b = input("Tweede getal? ")
getal_1 = float(a)
getal_2 = float(b)

# //calculator

if opera == "+":
    print("Result: ", getal_1 + getal_2)
elif opera == "-":
    print("Result: ", getal_1 - getal_2)
elif opera == "*":
    print("Result: ", getal_1 * getal_2)
elif opera == "/":
    if opera == "/" and getal_2 == 0:
        print("Kan niet delen door 0")
    else:
        print("Result: ", getal_1 / getal_2)
elif opera == "%":
    if opera == 0:
        print("Kan niet delen door 0")
    else:
        print("Result: ", getal_1 / getal_2)
else:
    print("Kan berekening niet uitvoeren.")