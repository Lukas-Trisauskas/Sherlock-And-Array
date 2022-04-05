def balanced_sum(arr):
    
    ptr = 0
    start = 0
    end = len(arr)
    
    lsa = 0
    rsa = 0
    
    result = False
    
    while(ptr < len(arr)):
        if(ptr == 0):
            rsa = sum(arr[ptr + 1:end])
            if(lsa == rsa):
                result = True
                break
            else:
                ptr += 1
        elif(ptr != 0):
            lsa = sum(arr[start:ptr])
            rsa = sum(arr[ptr + 1:end])
            if(lsa == rsa):
                result = True
                break
            else:
                ptr += 1
    if(result):
        return "YES"
    return "NO"

arr = [1, 2, 3, 3]
print(balanced_sum(arr))
