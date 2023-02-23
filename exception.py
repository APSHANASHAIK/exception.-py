from msvcrt import kbhit


print("enter the first number")
num1 = input()
print("enter the second number")
num2 = input()
try:
    print("the sum of two numbers",int(num1)+int(num2))
except Exception as k:
    print(k) 
    print("this is very important line")   

    