# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a) - 1
    found = -1

    while left <= right:
        mid_point = (left + right) // 2

        if x == a[mid_point]:
            found = mid_point
            break
        else:
            if x > a[mid_point]:
                left = mid_point + 1
            else:
                right = mid_point - 1

    return found

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
