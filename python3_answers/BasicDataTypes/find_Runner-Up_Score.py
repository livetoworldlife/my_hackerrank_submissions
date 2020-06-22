if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


if 2 <= n <= 10:
    zes = max(arr)
    i=0
    while(i<n):
        if zes == max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))
        
else:
    print("Please enter n between 2 and 10")

