#!/bin/python3

import math
import os
import random
import re
import sys
from dataclasses import dataclass

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

import heapq

def runningMedian(a):
    max_heap = []
    min_heap = []
    result = []

    for index, value in enumerate(a):
        if index % 2 == 0:
            heapq.heappush(max_heap, -1*value)
            
            if len(min_heap) == 0:
                root = -1*max_heap[0]
                result.append(float(root))
                continue
            
            if -1*max_heap[0] > min_heap[0]:
                toMin = -1*heapq.heappop(max_heap)
                toMax = heapq.heappop(min_heap)
                
                heapq.heappush(min_heap, toMin)
                heapq.heappush(max_heap, -1*toMax)
                
            root = -1*max_heap[0]
            result.append(float(root))
            
        else:
            toMin = -1*heapq.heappushpop(max_heap, -1*value)
            heapq.heappush(min_heap, toMin)
            
            root = (-1*max_heap[0]+min_heap[0])/2.0
            result.append(float(root))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

