
def reverse_string(input_str):    
    input_list = input_str.split('.')
    input_list.reverse()
    r_str = '.'.join(input_list)
    print(r_str)
    return  

if __name__ == '__main__':

    testcases = int(input())

    for tc in range(testcases):
        
        input_str = input()
        reverse_string(input_str)
