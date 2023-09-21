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
# 1 3 5 7 9

def miniMaxSum(arr):

    array = []

    for value in arr:
        try:
            if 1 <= value <= pow(10, 9):
                array.append(value)
                # print(f"The input number {value} is in the array.")
            else:
                # print(f"The input number {value} in the array is out of range.")
                raise StopIteration
        except StopIteration:
            # print("The operation is canceled.")
            return

    array.sort()

    # print(f"The sorted array is: {array}. \nThe minimum value is {array[0]} and the maximum value is {array[-1]}.")

    minimumSum = sum(array) - array[-1]
    maximumSum = sum(array) - array[0]

    print(f"{minimumSum} {maximumSum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
