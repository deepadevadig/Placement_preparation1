def getSum(number1,number2):
    return number1+number2

sum=getSum(12,45)
print("sum of number",sum)

sum1=getSum(12.8,45.6)
print("sum of number",sum1)

sum3=getSum("hello", "madam")
print("sum of ",sum3)

def getIntegersum(number1:int,number2:int):
    answer=number1 + number2
    return answer
    
answer1=getIntegersum(12.9,7.9)
print(answer1)
