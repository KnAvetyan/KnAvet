list_1=["ABC", 15, "efg", "d1"]
print (list_1[-2])

list_1.append("HIJ") #appending items to the list
print(list_1)

list_2=[]
list_2.append("apple")
list_2.append("orange")
list_2.append("peach")
print(list_2)

del list_2[1] #removing items from the list
print(list_2)

list_2.remove("apple") #removing items from the list
print(list_2)

list_3=[1, 2, 3, 4, 5, 6] 
if 2 in list_3:
    print ("true")
else:
    print ("false")

list_4=[1, 2, 3, 4, 5, 6] #looping through the list
for item in list_4:
    print (item)

list_5=["apple", "banana", "cherry"]
print(list_5[0])
list_5[0]="kiwi" #updating the value of the list
print(list_5[0])

list_6=["apple", "banana", "cherry"]
list_6.insert (1, "orange") #inserting an item to the list
print(list_6)

list_7=[1, 2, 3, 4, 5, 6]
list=list_7[2:5] #slicing the list
print(list)
list=list_7[:4]
print(list)
list=list_7[-3:]
print(list)
list=list_7[:-2]
print(list)
list=list_7[::2]
print(list)
list=list_7[1::2]
print(list)
list=list_7[::-1]
print(list)

print(max(list_7))
print(min(list_7))

new=(1,2,3,4,5,6) #tuples
print(list(new))

list_8=[4, 2, 1, 5, 8, 6]
list_8.append(12)
print(list_8)
list_8.remove(4)
print(list_8)
list_8.sort()
print(list_8)
list_8.reverse()
print(list_8.count(4))
list_8.extend([7, 9, 10])
print(list_8)
