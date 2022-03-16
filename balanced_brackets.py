#!/bin/python3

import os

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# {]}
table = {
    "}": "{",
    "]": "[",
    ")": "(",
}
    # [](){()}
def isBalanced(s):
    stack = []
    
    for char in s:
        if char not in table:
            stack.append(char)
            continue
        
        if len(stack) == 0:
            return "NO"
            
        if stack.pop() != table[char]:
            return "NO"
    
    if len(stack):
        return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

    
