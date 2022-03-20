#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

from collections import deque
sys.setrecursionlimit(10000)

class Node():
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
        
def create(root, indexes):
    queue = deque([root])

    # traverse the indexes
    for left, right in indexes:
        temp = queue.popleft()
        
        # left child
        if left != -1:
            temp.left = Node(left)
            queue.append(temp.left)
            
        # right child
        if right != -1:
            temp.right = Node(right)
            queue.append(temp.right)

    return root

def swap(root, query, level, l):
    if root:
        if level % query == 0:
            # swap the nodes
            root.left, root.right = root.right, root.left
            
        # inorder traversal
        swap(root.left, query, level+1, l)
        l.append(root.info)
        swap(root.right, query, level+1, l)

def swapNodes(indexes, queries):
    # Create the tree
    root = Node(1)
    root = create(root, indexes)
    
    result = []
    # Process the queries
    for query in queries:
        l = []
        swap(root, query, 1, l)
        result.append(l)
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

