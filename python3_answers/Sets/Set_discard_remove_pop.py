n = int(input())
s = set(map(int, input().split()))
N = int(input())

while N >= 1:
    a = list(map(str, input().split()))
    
    N -= 1
    if a[0] == "pop":
        s.pop()
    elif a[0] == "remove":
        s.remove(int(a[1]))
    elif a[0] == "discard": 
        s.discard(int(a[1]))
    else:
        print("please again")   


num = sum(s)
print(num)        
