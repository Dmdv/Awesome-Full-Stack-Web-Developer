# Uses python3
import sys
import random

def is_sorted(items, descending=False):
    for i in range(len(items)):
        if i > 0 and descending is False and items[i] < items[i - 1]:
            return False
        elif i > 0 and descending and items[i] > items[i - 1]:
            return False

    return True

def partition3(a, l, r):
    x = a[l]
    j = l
    k = l

    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[j] = a[j], a[l]
    return j, k

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    n, m = partition3(a, l, r)
    randomized_quick_sort(a, l, n - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)

    assert is_sorted(a)

    for x in a:
        print(x, end=' ')
