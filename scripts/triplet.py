def triplet_sum(n,arr):

    triplet_count = 0
    print(arr)
    arr.sort()
    print(arr)
    i = n-1
    while(i>=0):
        j=0
        k=i-1
        print (i,j,k)
        while(j<k):

            sum_num = arr[j] + arr[k]
            if sum_num == arr[i]:
                print (arr[j],arr[k])
                triplet_count += 1
                j += 1
                k -= 1
            elif sum_num < arr[i]:
                j += 1
            elif sum_num > arr[i]:
                k -= 1
        i -= 1

    if triplet_count > 0:
        print (triplet_count)
    else:
        print("-1")        

return

             




def get_triplet(n,arr):
    
    tripletcount = 0
    
    for i in range(n-1):
        j = i+1        
        while (j<n):
            #print (j,i)
            sum_trip = arr[i] + arr[j]
            if sum_trip in arr:
                #print(arr[i],arr[j])
                tripletcount += 1
            j += 1

    if tripletcount > 0:
        print (tripletcount)
    else:
        print("-1")

    return
        


if __name__ == '__main__':

    testcases = int(input())

    for tc in range(testcases):

        size = int(input())
        arr = list(map(int,input().split()))

        #get_triplet(size,arr)
        triplet_sum(size,arr)

