length =12
Width =23
Area = length*Width
print (Area)
f=15
print (f)
f= 'Hallo'
print (f)
a, b, c, d = 5, 17, 48, "hello"
print (a)
print (b)
print (c)
print (d)
a = 100, 200, 300
print (a)
print (type (a))
a, *b = 123, 456, 789
print (a)
print (type (a))
print (b)
print (type (b))
x= 12.3
y= 13.4
z= float(x)+float(y)
print (z)
x= 12.3
y= 13.4
z= int(x)+int(y)
print (z)
x=18
y=4
print ('x+y=', x+y)
print ("x-y=", x-y)
print ("x*y=", x*y)
print ("x/y=", x/y)
print ("x//y=", x//y)
print ("x**y=", x**y)
print ("x%y=", x%y)


string_1= "Hi "
string_2=string_1 + "Hallo"
print (string_2) 
var1='Hello how are you'
var2= "welcome"
print (var1[7:], var1[0])
print (var2[4:6])
print ("o" in var1)
print ("hi" not in var1)

name= 'Knarik'#formating
age= 39
print (f'hello {name}, you are {age} years old')
name=input ("Enter your name")
salary=input ("Write your salary")
company= input ("where do you work")
print ("print employee details")
print ("name",  name)
print ("company",company)
print ("Salary", salary)

name= "arpi" 
age=10
print ("Hello, %s, you are %s years old" % (name, age))

name="Hamlet"
age=8
print ("Hello, you are {}. You are {} years old.". format (name, age))

name= "Hayk"
surname="Kach"
age=2
print (f"This is {name}, {surname}, he/she is {age} years old")
print ("this is {},{}, he is {} years old.". format (name, surname, age))
print ("This is %s, %s. He is %s years old." %(name, surname, age))

text="This is a banana. The banana is yellow" #count
x=text.count("banana",5, 34)          
print(x)

text="This is a banana. The banana is yellow"#find
x=text.find ("banana")
x= text.find ("apple")
print(x)

text1="Hello"#join
text2="World"
x=" ".joint([text1,text2])
x=" ".join([text1, "beautiful", text2])
words=["Hi","I","am","Knarik"]
x=" ".join(words)
print(x)

text1="I like apple"# replace
text2=text1.replace("apple","peach")
print(text2)

text1="I like skiing" #split
x=(text1.split(" "))
x=(text1.split ("i"))
print(x)

text1="I like apples" #upper
print (text1.upper())

string="12345" #reversed
x="".join(reversed(string))
print(x)

text1="hello world"
x=len(text1)
print(x)

a="abc"
b="xyz"
new_a=b[:2]+a[2:]
new_b=a[:2]+b[2:]
print (new_a+" "+ new_b)