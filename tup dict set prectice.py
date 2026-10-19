tup_1=("apple", "banana", "cherry")
tup_2=("orange", "kiwi", "melon")
tup_3=tup_1+tup_2 #concatenating tuples
print(tup_3)
print (tup_3[::-1])

list_1=["apple", "banana", "cherry", "orange",]
print ("Favourit fruit:",list_1[2])
list_1.append ("banana")
list_2=(list(set(list_1)))
print ("fruits without duplicates:", list_2) #updating the value of the list

dict_1={"name": "Ann", "surname":"Smith", "age": 30, "city": "London"}
dict_1["name"]= "Arpi"
dict_1['job'] = "Engineer"
print( len(dict_1))
print(dict_1)
print(type(dict_1))
dict_1.pop ("surname")

print(dict_1.keys())
print (dict_1.values())

set_1={"apple", "banana", "cherry"}
set_2={"orange", "kiwi", "banana"}
set_3=set_1|set_2
set_3=set_1.union(set_2)
set_4=set_1&set_2
set_4=set_1.intersection(set_2)
set_5=set_1-set_2
set_5=set_1.difference(set_2)
print(set_3)
print(set_4)
print(set_5)