mylist=[5,6,0,2,0,1,7]
print(mylist)
for i in mylist:
  if i==0:
    mylist.remove(i)
    mylist.append(i)
print(mylist)