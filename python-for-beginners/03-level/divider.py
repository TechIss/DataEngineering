try:
    getal_1 = input("Eerste getal? ")
    getal_2 = input("Tweede getal? ")
    result = input(float(getal_1)/float(getal_2))
except ZeroDivisionError:
    result1 = str(float(0))
    print("Kan niet delen door 0")

if input != result:
    print("Resultaat: " + str(float(getal_1) / float(getal_2)))

#     result = print("Kan niet delen door 0")
# else:
#     print("Result: " + result)
