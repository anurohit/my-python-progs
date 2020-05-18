
def swap_case(str):

    new_string = ''

    for chr in str:
        
        if chr.isupper():
            chr = chr.lower()
        elif chr.islower():
            chr = chr.upper()
        
        new_string += chr

    print (new_string)

if __name__ == '__main__':

    str = input()

    swap_case(str)