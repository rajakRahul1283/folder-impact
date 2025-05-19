import math

n = int(input("enter the number of element:"))
a = list(map(int, input("Enter your list: ").split()))
count = 0

for i in range(n):
    num = a[i]
    x = 1
    y = int(round(num ** (1/3)))  
    while x <= y:
        z = x**3 + y**3
        if z == num:
            count += 1
            break
        elif z > num:
            y -= 1
        else:
            x += 1

print(count)
