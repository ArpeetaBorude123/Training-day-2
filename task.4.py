#i/p=[1,2,3,4]
#o/p=[24,12,8,6]

array = [1, 2, 3, 4]

result = []

for i in range(len(array)):
    product = 1

    for j in range(len(array)):
        if i != j:
            product = product * array[j]

    result.append(product)

print(result)
