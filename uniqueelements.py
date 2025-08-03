def print_unique_elements(numbers):

    for readIndex in range(0, len(numbers),1):
        is_dupicate = False
        
        for compareIndex in range( 0, len(numbers), 1):
            if readIndex == compareIndex:
                continue
            if numbers[readIndex] == numbers[compareIndex]:
                is_dupicate = True
                break
        if(is_dupicate == False):
                print(numbers[readIndex])

input1=[1,2,2,4,9]

print_unique_elements(input1)
