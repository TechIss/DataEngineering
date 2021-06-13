a = int(input("Wat is de score van speler 1? "))
b = int(input("Wat is de score van speler 2? "))

if a > b:
    print("Speler 1 heeft gewonnen!")
elif a < b:
    print("Speler 2 heeft gewonnen!")
else:
    if a == b:
        print("Speler 1 en speler 2 hebben gelijk gespeeld!")
        