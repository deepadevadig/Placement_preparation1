def get_minmax(numbers):

    max = numbers[0]
    min = numbers[0]

    for index in range(1,len(numbers),1):
        if numbers[index] > max:
            max = numbers[index]

        if numbers[index] < min:
            min = numbers[index]     


    return max,min      

input1=[1,6,0,98]  
resultmax,resultmin=get_minmax(input1)
print(f"maximum value={resultmax}  minimum value={resultmin}")

