num = [1, 3, 5, 7, 1, 12, 14, 4, 4]
print(num)

i = 0
x = int(input("enter the value of you want to find\n"))

while i <= len(num):
    if num[i] == x:
        print("----position is----\n", i)
        if i <= len(num):
            found = True
            print("----position is----\n", i)
            break
    else:
        if num[i] > x:
            print("value is small not matched still finding.....", i)
            print("exiting.........................")
        else:
            print("value is greater not matched still finding.....", i)
            print("exiting.........................")
                
            
    i += 1

