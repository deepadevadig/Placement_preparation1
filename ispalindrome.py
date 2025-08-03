def is_pallindrome(string):


    leftindex = 0
    rightindex = len(string)-1

    while(leftindex < rightindex):

        if string[leftindex] != string[rightindex]:

            print("its not a pallindrome")

            break
        else:
            print("it is a pallindrome")
            
        leftindex += 1
        rightindex -= 1
    

input1="121"
is_pallindrome(input1)
