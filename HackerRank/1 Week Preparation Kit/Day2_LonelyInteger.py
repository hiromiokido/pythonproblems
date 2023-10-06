#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):

    lonelyInteger = []

    try:
        if (n >= 1) & (n < 100):
            if (n % 2 != 0):
                for index, value in enumerate(a):
                    if (index >= 0) & (index < n):
                        if (value >= 0) & (value <= 100):
                            if (a.count(value) == 1):
                                lonelyInteger.append(value)
                        else:
                            print("The value in the list is not in the limited range.")
                            raise StopIteration
                    else:
                        print("The value is not between 0 < value < n.")
                        raise StopIteration
            else:
                print("n is not an odd number.")
                raise StopIteration
        else:
            print("The value n isn't in the limited range.")
            raise StopIteration
    except StopIteration:
        return

    try:
        if len(lonelyInteger) == 0:
            print("There's no unique element")
            raise StopIteration
        else:
            return lonelyInteger[0]
    except StopIteration:
        return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(f"Result: {result}")

    # fptr.write(str(result) + '\n')

    # fptr.close()
