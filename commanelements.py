# def commanelements(input1, input2):
#      for input1_Index in range(0 , len(input1), 1):
#           is_Found = False

#           for input2_Index in range( 0, len(input2), 1):
               
#                if input1_Index == input2_Index:
#                     continue
               
#                if input1[input1_Index] == input2[input2_Index]:
#                     is_Found = True
#                     break
#           if is_Found:
                    
#             print(input1[input1_Index])

# number1 = [1,2, 3, 4]
# number2=[1,6,3,5] 
# commanelements(number1,number2)    
# 
def commanelements(input1, input2):
    for element in input1:
        if element in input2:
            print(element)

# Example usage
number1 = [0, 2, 3, 4]
number2 = [1, 6, 3, 5]
commanelements(number1, number2)
               

