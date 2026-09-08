mylist = [2, 4, 6, 8, 9, 1, 5]

even = 0
odd = 0

for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even", even)
print("Odd", odd)
