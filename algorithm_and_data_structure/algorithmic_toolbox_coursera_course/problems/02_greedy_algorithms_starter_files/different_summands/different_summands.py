# Uses python3
import sys
import math


def form_output(prizes, winners):
    a = []
    won_prizes = 0
    for i in range(1, winners):
        a.append(i)
        won_prizes += i
    a.append(prizes - won_prizes)
    return a

def optimal_summands(n):
    if (n == 1):
        return [1]

    a = 1
    b = 1
    c = -2 * n

    d = b**2-4*a*c

    if d < 0:
        return 'error'
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        return form_output(n, math.floor(x))
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        if(x1 > 0):
            return form_output(n, math.floor(x1))
        else:
            return form_output(n, math.floor(x2))

def test():
    print(optimal_summands(10))
    print(optimal_summands(1000))
    print(optimal_summands(1))
    print(optimal_summands(4))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
