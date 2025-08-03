def print_ascii(string):
    for ecachcharacter in string:
        value=ord(ecachcharacter)
        print(f" {value} -----{ecachcharacter}")

print_ascii("hello goodmorning")