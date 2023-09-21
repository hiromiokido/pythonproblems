import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# -4 3 -9 0 4 1

def plusMinus(arr):
    total = len(arr)
    positive, zero, negative = [], [], []

    for integer in arr:
        if integer > 0:
            positive.append(integer)
        elif integer < 0:
            negative.append(integer)
        else:
            zero.append(integer)

    total_positives = len(positive)
    total_negatives = len(negative)
    total_zero = len(zero)

    positive_ratio = total_positives/total
    negative_ratio = total_negatives/total
    zero_ratio = total_zero/total

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    try:
        # n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        plusMinus(arr)

    except ValueError as e:
        raise e
    