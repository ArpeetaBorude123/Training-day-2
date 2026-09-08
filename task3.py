# i/p= [7,3,9,2,8]
# o/p= second largest

array = [7, 3, 9, 2, 8]

largest = array[0]
second_largest = array[0]

for i in range(len(array)):
    if array[i] > largest:
        second_largest = largest
        largest = array[i]
    elif array[i] > second_largest and array[i] != largest:
        second_largest = array[i]

print("Second largest =", second_largest)