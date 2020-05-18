
def find_missing(n,arr):

    total_sum = sum(range(1,n+1))
 
    missing_num = total_sum - sum(arr)  

    print(missing_num)

if __name__ == '__main__':

    testcases = int(input())

    for tc in range(testcases):

        size = int(input())
        arr = list(map(int,input().split()))

        find_missing(size,arr) 