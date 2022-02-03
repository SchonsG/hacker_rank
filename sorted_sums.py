
"""
Example:
n = 3
a = [9, 5, 8]

s1 = f(1) = 1*9 = 0
s2 = f(2) = 1*5 + 2*9 = 23
s3 = f(3) = 1*5 + 2*8 + 3*9 = 48
f(n) = f(1)+f(2)+f(3) = 9 + 23 + 48 = 80

"""

n = 3
a = [9, 5, 8]

def main():
    result = 0
    helper = []

    for value in a:
        helper.append(value)
        helper.sort()

        for index, value in enumerate(helper):
            result += value*(index+1)

    print(result)


if __name__ == "__main__":
    main()

