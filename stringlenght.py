def get_string_length(string):
    counter=0

    if string==None:
        print("invalid type")
        
    else:

        for eachcharacter in string:
            counter=counter+1


            print(f"{counter}--is the length of---{string}")

input1=None
get_string_length(input1)