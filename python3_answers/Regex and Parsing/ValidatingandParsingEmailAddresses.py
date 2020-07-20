import re
import email.utils

n = int(input())
for i in range(n):
    a, b = input().split(" ")
    
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', b)
    if m:
        print(a,b)
