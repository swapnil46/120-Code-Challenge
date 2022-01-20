#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    m=n
    for i in range(n):
        print(" "* (m-1)+ "#"*(i+1))
        m-=1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
