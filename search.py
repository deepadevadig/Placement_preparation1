def search(numbers, key):
    leftIndex = 0
    rightIndex = (len(numbers)-1)
    found = False

    while (leftIndex <= rightIndex):
        middleIndex = int(leftIndex + (rightIndex - leftIndex) / 2)

        if numbers[middleIndex] == key:
            found = True
            break

        if numbers[middleIndex] > key:
            rightIndex = middleIndex - 1
        else:
            leftIndex = middleIndex +1
    return found
input1=[1,2,3,4,5,89]  
key=8
result=search(input1,key)    

if result:
    print(f"number is found  ")
    
else:
    print("number not found")


