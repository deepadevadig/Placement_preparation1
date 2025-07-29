number="0000"
def isdigit(number):
    
    for eachcharacter in number:
        if eachcharacter >='0' and eachcharacter <= '9':
            print("it is a digit")
            break
        else:
            print("it is not a dihgit")
            break

isdigit(number)