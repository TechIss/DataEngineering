
opera = input("Welke operatie wil je uitvroeren? (+, -, *, / of %) ")

# //Vraag operatie
if opera not in "/*-+%":
    exit(print(opera, "is geen geldige operatie, probeer +, -, *, / of %"))

# //Float
try:
    a = input("Eerste getal? ")
    b = input("Tweede getal? ")
    getal_1 = float(a)
    getal_2 = float(b)
except ValueError:
    exit(print("Kan ", getal_1, " niet omzetten naar een getal, probeer een '.' ipv ',' te gebruiken"))

# //calculator

if opera == "+":
    print("Result: ", getal_1 + getal_2)
elif opera == "-":
    print("Result: ", getal_1 - getal_2)
elif opera == "*":
    print("Result: ", getal_1 * getal_2)
elif opera == "%":
    if opera == "%" and getal_2 == 0:
        print("Kan niet delen door 0")
    else:
        print("Result: ", getal_1 % getal_2)
elif opera == "/":
    if opera == "/" and getal_2 == 0:
        print("Kan niet delen door 0")
    else:
        print("Result: ", getal_1 / getal_2)
else:
    print("Kan berekening niet uitvoeren.")
