def get_no_of_vowels(string):

    counter=0
    if string!=None:
        for eachcharacter in string:
            if(eachcharacter=='a' or
              eachcharacter=='e' or
              eachcharacter=='i' or
             eachcharacter=='o' or
              eachcharacter=='u' or
              eachcharacter=='A' or
              eachcharacter=='E' or
              eachcharacter=='I' or
              eachcharacter=='O' or
              eachcharacter=='U' ):

              counter=counter+1
        print(f" given {input} and number of vowels is  {counter}")
              
input="Deepa"
get_no_of_vowels(input)



                    
