def swapnumber(item1,item2):
    temp=item1
    item1=item2
    item2=temp
    return item1,item2

number1=12
number2=20
print(f"before swapping number1={number1} number2={number2}")

number1, number2=swapnumber(number1,number2)

print(f"swapping after number1={number1} number2={number2}")



def swapSimple(item1,item2):
    return item2,item1
num1=23
num2=34

num1,num2=swapSimple(num1,num2)
print(f"after swapping num1={num1},num2={num2}")