# for getal in range(20):
#    if getal % 2 == 1:
#        print(getal)

n = range(1, 101)
for x in n:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
