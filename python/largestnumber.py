x = int(input("Enter the first number "))
y = int(input("Enter the second number "))
z = int(input("Enter the third number "))
if (x == y and y == z and x == z):
    print("All are equal")
elif (x > y and x > z):
    print(x, "is the largest number")
else:
    if (y > x and y > z):
        print(y, "is the largest number")
    else:
        print(z, "is the largest number")