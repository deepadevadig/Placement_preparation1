def reversestring(string):
    reversestring1=""
    length=len(string)
    
    print(f"length={length}")
    
    for end in range(length-1,-1,-1):
        reversestring1+=string[end]

    print(reversestring1)   
name="xyz"
print(f"before reverse={name}")
reversestring(name)

