num = int(input("Van welk getal wil je de faculteit weten? "))
factorial = 1

for i in range(1,num + 1):
    factorial = factorial*i

print("The factorial of",num,"is",factorial)
