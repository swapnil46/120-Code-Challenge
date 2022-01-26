#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sm=0
    s=0
    arr=sorted(arr)
    n=len(arr)
    for i in range(n-1):
        sm=sm+arr[i]
    for i in range(1,n):
        s=s+arr[i]
    print(sm,s)
    
    
 
 
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
