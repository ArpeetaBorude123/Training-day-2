# i/p: [5,3,2,9,8]
# o/p: max=9, min=2

array=[5,3,2,9,8] #array=5
print (array)
max=min=array[0] # min | = 9 max=2
for i in range (len(array)): #i=1 <5
    if array[i]>max: 
        max=array[i]
    if array[i]<min:
        min=array[i]
print("Min",min)
print("Max",max)

