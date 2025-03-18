# import random



# print statement
print("Hello World from Komal")

# print name by taking User Input
name = input ("Enter your name: ")
print("Hello, "+ name+"!")

#Simple Math Calculation:

# Addition
num1 = int(input ("Enter first number: "))
num2 = int(input ("Enter second number: "))
sum = num1 + num2
print("The Sum of the numbers is: " , sum)


# Subtraction
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
subtract = num3 - num4
print("Difference between two numbers is: ", subtract)


#Multiplication
num5 = int(input("Enter first number: "))
num6 = int(input("Enter second number: "))
multiply = num5* num6
print("Product of two numbers is: ", multiply)


#Division
num7 = int(input("Enter first number: "))
num8= int(input("Enter second number: "))
if num8 !=0:
    Divide = num7/num8
    print("Division of two numbers is:", Divide)
else:
    print("Cannot divide by zero")


#Modulus
num9 = int(input("Enter first number: "))
num10 = int(input("Enter second number: "))
if num10 != 0:
    modulus = num9%num10
    print("Modulus is: ", modulus)
else:
    print("Second number must be non zero")


#Exponent
num11 = int(input("Enter first number: "))
num12 = int(input("Enter second nnumber: "))
exponent = num11**num12
print("Exponent is: ", exponent)


#Floor Division
num13 = int(input("Enter first number: "))
num14 = int(input("Enter second number: "))
if num14 !=0:
    floor_division = num13//num14
    print("Floor Division is: ", floor_division)
else:
    print("Cannot perform floor division. Second number must be non-zero")


# This is  a single line comment

a =int(input("Enter a number: "))
print(type(a))                  # returns 'int'

b = input("enter a number: ")
print(type(b))                  # returns 'str'



first_name = "Komal"
last_name = "Abbasi"
email = f"""Hi {first_name} {last_name},
        We are glad to inform to inform you that you have been selected for next quarter.
        Many mnay Congratulations!"""
print(email)


print(f" Hi {first_name} {last_name} \t Good morning!")

print("We ae glad. \nKeep it up!")
print("We ae glad. \tKeep it up!")

#index     0          1         2        3         4
fruits = ["Apple", "Banana", "Carrot", "Door", "Eggplant"]
#          -5         -4        -3       -2       -1


print(len(fruits))
print(fruits[1])
print(fruits[1:5])
print(fruits[4])
print(fruits[-2])
print(fruits[-1])



msg = "Hello Komal"
print(msg[3:8])
print(msg[4])


msg = f"""abcdefghijklmnopqrst
qwertyuiiplkjhgfdsaa
mnbvcxxzasdfghhjkpo"""
print(msg.split("\n"))



byte_data:bytes = b"Hello"
byte_data[1] = 22 # cannot assign anything. it is immutable
print(byte_data[1])


pak = ['a', 'b', 'c', 'd', 'e']
print(", ".join(pak))


msg = "Hello world"
print(msg.replace("hello", "Hi"))



runs = random.randint(0,150)
print(runs)

balls = 49
if runs>100 and balls<runs:
    print("🔔 King")
else:
    print("Try Again!")



user1 = {
    "name":"Komal",
    "age":28,
    "is_married": True
}
print(user1["name"])


num = ['a','b', 'c']
print(num.pop())
print(num.append('z'))
print(num)


num = {'a', 'b', 'c', 'd','a'}
print(num)



is_teacher = True
print(id(is_teacher))



a = 'Komal'
b = "Abbasi"
c = a + " " +b
print(c)

a = 12
b = float('12')
print(a+b)

a =( "Komal","Abbasi", "Maha")
a[0]="Sana" 
print(a)


a = [1, 2, 3, 4, 5, 6, 1, 2, 6] 
b = {1, 2, 3, 4, 5, 6, 1, 2, 6}
print(a)
print(b)


def greet():
    print("Hello function")
print("Hello")

greet()


def greet(name):
    print(f"Hello from {name}")
    return "Returned from Function"
print("Hello")
greet("Komal")


def greet(name):
    print(f"Hello from {name}")
    return "Returned from function"
returned_value = greet("Okasha")
print(returned_value)


num = [1, 2, 3, 4, 5]
for i in num:
    print (i)

a = set(range(1,11))
print(a)

print(list(range(1,5)))


range_fn = range(1,15)
for num in range_fn:
    print(num)

num = iter(range(1,11))
while True:
    try:
        print(next(num))
    except StopIteration:
        break

iftar = ["samosay", "pakoray", "sharbat"]
iftar[2] = "chaat"
iftar.pop()
iftar.append("Dahi phulki")
iftar.remove("samosay")
print(iftar)

#tuple-count
iftar = ("samosay", "pakoray", "sharbat", "pakoray", "pakoray")
print(iftar.count("pakoray"))

#tuple-index
iftar = ("chat","samosay", "pakoray", "sharbat", "pakoray", "pakoray" )
print(iftar.index("sharbat"))

iftar = ("chat","samosay", "pakoray", "sharbat", "pakoray", "pakoray" )
print(set(iftar))
print(list(iftar))

iftar = ["chat","samosay", "pakoray", "sharbat", "pakoray", "pakoray"]
print(set(iftar))
print(tuple(iftar))


iftar = {"chat","samosay", "pakoray", "sharbat", "pakoray", "pakoray"}
print(list(iftar))
print(tuple(iftar))

iftar = {'samosay', 'pakoray'}
iftar.remove("pakoray")
iftar[0] = "chaat"
print(iftar)


i = 1
while i<=10:
    print(i)
    i = i+1


num = iter(range(1,5))
while True:
    try:
        print(next(num))
    except StopIteration:
        break


num = range(1,10)
for i in num:
    print(i)

num = iter(range(1, 10))
while True:
    try:
        print(next(num))
    except StopIteration:
        break

num = iter([1, 2, 3, 4])
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


num = iter([10, 20, 30, 40])
while True:
    try:
        print(next(num))
    except StopIteration:
        print("Iteration Finished")
        break


def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


def my_fn():
    return [1, 2, 3]
print(my_fn())

def infinite_num():
    num = 1
    while True:
        yield num
        num +=1
gen = infinite_num()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def countdown(n):
    while n>0:
        yield n
        n-=1
for num in countdown(5):
    print (num)

# Listof numbers
my_list = [1, 2, 3, 3, 5,1, 2, 3, 3, 5, ]
print(len(my_list))

# Mixed List
mixed = ["Komal", True, 1, 3.254]
print(mixed[-4])

# Changing List element
mixed = ["Komal", True, 1, 3.254]
mixed[3] = "Sana"
print(mixed)

# Adding List element by append() and insert() method
mixed = ["Komal", True, 1, 3.254]
mixed.append("Asma")
mixed.insert(1, "Hira")
print(mixed)


# Removing elements from List by pop(), remove() and del()
mixed = ["Komal", 1, True, 3.254]
# mixed.pop(0)
# del mixed[0]
mixed.remove(next(x for x in mixed if x is True))
print(mixed)

mixed = ["Komal", 1, True, 3.254,  False, "", None]
mixed.remove(next(x for x in mixed if x is not True))
print(mixed)

mixed = ["Komal", 1, True, 3.254,  False, "", None]
mixed = [x for x in mixed if x != True]
print(mixed)


mixed = ["Komal", 1, True, 3.254,  False, "", None]
mixed.clear()
print(mixed)


# Looping through a list   
mixed = ["Komal", 1, True, 3.254,  False, "", None]
for i in mixed:
    print(i)


mixed = ["Komal", 1, True, 3.254,  False, "", None]
i=0
while i < len(mixed):
    print(mixed[i])
    i +=1

mixed = ["Komal", 1, True, 3.254,  False, "", None]
print(mixed[1:3])
print(mixed[:3])
print(mixed[2:])
print(mixed[::1])
print(mixed[::2])
print(mixed[::3])
print(mixed[::4])


numbers = [x*2 for x in range(1, 6)]
print(numbers)

numbers = [x**2 for x in range(1, 6)]
print(numbers)



# Tuples
my_tup = (1, True, "Komal", 3.1258)
print(my_tup[1])

single_tup = ("Komal",)
print(single_tup)
