#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#




def breakingRecords(scores):
    # Write your code here
    m=scores[0]
    mi=scores[0]
    countm=0
    countmi=0
    for i in range(1,n):
        if(scores[i]>m):
            m=scores[i]
            countm+=1
        if(scores[i]<mi):
            mi=scores[i]
            countmi+=1
    return countm,countmi
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
