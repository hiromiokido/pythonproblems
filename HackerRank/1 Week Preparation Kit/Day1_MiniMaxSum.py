#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    
    arr.sort()
    max_arr = arr[-1]
    
    countArray = []
    
    for index_array in range(n):
        countArray.append(0)
        
    try:
    
        if (n >= 100) & (n <= pow(10, 6)):
            
            for index, value in enumerate(arr):
                
                if (index < n) & (index >= 0):
                    
                    if (value >= 0) & (value < 100):
                        print(countArray[value])
                        print(arr.count(value))
                        # countArray[value] = arr.count(value)

                    else:
                        print("value is not in the limited range.")
                        raise StopIteration
                    
                else:
                    print("Index is not in the limited range.")        
            
        else:
            print("n is not in the limited range.")
            raise StopIteration
    
    except StopIteration:
        return
    
    

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

