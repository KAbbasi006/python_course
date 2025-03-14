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
