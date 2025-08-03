def bitbinaryform(number):
    no_of_bits=number.bit_length()

    print(f" number of bits= {no_of_bits}")
    mask=1
    mask=mask << no_of_bits-1

    for _ in range(no_of_bits):
        if(number & mask):
            print("1", end="")
        else:
            print("0",end="")

  
  
        mask >> 1
input = 1024
bitbinaryform(input)    
    





