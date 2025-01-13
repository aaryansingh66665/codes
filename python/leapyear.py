k = int(input("Enter the number "))
if k % 400 == 0:
    print("Leap year")
elif k % 4 == 0 and k % 100 != 0:
    print("leap year")
else:
    print("not a leap year")