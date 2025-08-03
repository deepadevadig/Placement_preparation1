def getwordcount(string):
    counter = 0
    for char in string:
        if char == ' ' or char == '\t' or char == '\n':
            counter += 1

    # Only print once
    if counter == 0:
        print("Number of words = 1")
    else:
        print(f"Number of words = {counter + 1}")
        
input = "hello"
getwordcount(input)
