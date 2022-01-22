#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    countp=0
    countn=0
    countz=0
    for i in range(n):
        if(arr[i]>0):
            countp+=1
        elif(arr[i]<0):
            countn+=1
        else:
            countz+=1
    p=countp/n
    ne=countn/n
    z=countz/n
    print("%.6f"%p)
    print(format(ne,'.6f'))
    print(format(z,'.6f'))
    
  
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
