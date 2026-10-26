N = int(input("Enter N: "))

a, b = 0, 1
while a < N:
    print(a, end=" ")
    a, b = b, a + b
print()
