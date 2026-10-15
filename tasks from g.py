temps=[12,18,25, 30, 22, 19,15]
temps1=temps [2:5]
print(temps1)

tup=("dog", "cat", "rabbit", "bird", "fish")
list1=list(tup)
print (list1[2])

numbers=[14, 5, 29, 8, 42, 19]
max_num=numbers[0]
for item in numbers:
    if item>max_num:
        max_num=item
print (max_num) 