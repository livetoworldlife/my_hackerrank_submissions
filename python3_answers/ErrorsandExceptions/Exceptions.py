#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(*n):
    for i in n:
        i = i.split(" ")
        try:
            m = int(i[0]) // int(i[1])
            return m
        except ZeroDivisionError as e:
            return("Error Code: {}".format(e))
        except ValueError as e:
            return("Error Code: {}".format(e))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = str(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
