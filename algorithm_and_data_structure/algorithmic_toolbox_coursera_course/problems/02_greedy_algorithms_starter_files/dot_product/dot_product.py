#Uses python3

import sys

def max_dot_product(a, b):
    res = 0
    a_s = sorted(a, reverse=True)
    b_s = sorted(b, reverse=True)
    for i in range(len(a)):
        res += a_s[i] * b_s[i]
    return res

def test():
    a = [23]
    b = [39]
    print(max_dot_product(a, b))

    a = [1, 3, -5]
    b = [-2, 4, 1]
    print(max_dot_product(a, b))

if __name__ == '__main__':

#    test()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
