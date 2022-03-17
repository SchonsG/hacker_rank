#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class Node():
    def __init__(self):
        self.children = {}
        self.size = 0
        
    def __repr__(self):
        return repr(self.children)

    def __get_char_ascii(self, char):
        return ord(char)
    
    def add(self, word):
        self._add(word, 0)
        
    def _add(self, word, index):
        self.size += 1

        if len(word) == index:
            return
        
        letter = word[index]
        ascii_value = self.__get_char_ascii(letter)
        
        child = self.children.get(ascii_value)
        
        if child is None:
            child = Node()
            self.children[ascii_value] = child
        
        child._add(word, index + 1)
        
    def find(self, word):
        return self._find(word, 0)
        
    def _find(self, word, index):
        if len(word) == index:
            return self.size

        letter = word[index]
        ascii_value = self.__get_char_ascii(letter)
        
        child = self.children.get(ascii_value)
        
        if child is None:
            return 0
        
        return child._find(word, index+1)

def contacts(queries):
    node = Node()
    result = []
    
    for query in queries:
        if query[0] == 'add':
            node.add(query[1])
        else:
            result.append(node.find(query[1]))
            
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
