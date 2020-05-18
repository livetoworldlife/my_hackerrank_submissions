import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if  0 < n < 101:
    if (n%2 == 1) or (n in range(6,21) and n%2 == 0):
        n = "Weird"
    elif (n%2 == 0 and n in range(2,6)) or (n > 20 and n%2 == 0):
        n = "Not Weird"      

print(n)