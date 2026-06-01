num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
num4 = int(input("enter fourth number: "))
if(num1>=num2 and num1>=num3 and num1>=num4):
    print("the largest number is ",num1)

elif(num2>=num3 and num2>=num4):
    print("the largest number is ",num2)
elif(num3>=num4):
    print("the largest number is ",num3)
else:
    print("the largest number is ",num4)