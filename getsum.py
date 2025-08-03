def getsum(numbers):

    sum=0
    
    for number in numbers:
        sum=sum+number
    return sum
numbers=[1,4,2]
final=getsum(numbers)
print(final)