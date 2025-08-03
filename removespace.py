def remove_space_in_string(string):
    output=""

    for char in string:
        if char !=' ' and char !="\t" and char != '\n':
            output = output + char
    print(output)


input="hello word"   
remove_space_in_string(input)
