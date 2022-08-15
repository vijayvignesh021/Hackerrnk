def insertionSort1(n, arr):
    checker = arr[n-1]
    i = n-2
    while(arr[i]>checker and i >=0):
        arr[i+1] = arr[i]
        print(*arr,sep=' ')
        i -= 1
    if arr[i] < checker:
        arr[i+1] = checker
        print(*arr,sep=' ')
    else:
        arr[0] = checker
        print(*arr,sep=' ')