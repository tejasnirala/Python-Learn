var1 = "hello "
var2 = "Tejas"
var3 = 4
var4 = 36.7

var5 = "32"
var6 = "54"
print(type(var1), end=" -> ")
print(var1)
print(type(var2), end=" -> ")
print(var2)
print(type(var3), end=" -> ")
print(var3)
print(type(var4), end=" -> ")
print(var4)

print(var1 + var2)
print(var3 + var4)

print(var5 + var6)  # This line will treat var5 and var6 as strings

# Typecasting
print(
    int(var5) + int(var6)
)  # This line will treat var5 and var6 as integers due to typecasting

"""
Some typecasting functions are -
    int()
    str()
    float()

"""

print(10 * var1)  # This will print hello 10 times like for loop

print("Enter a number - ", end="")
inpnum = input()
print("You entered -", inpnum)
print(
    "Sum -", int(inpnum) + 10
)  # This will perform the calculation as we typecasted it to integer

# This will throw error because inpnum is string not an integer
# print("You entered -",inpnum + 10)
