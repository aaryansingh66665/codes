x = int(input("enter the number\n"))
squares = [i**2 for i in range(1, int(x**0.5) + 1)]
print(" ".join(map(str, squares)))

