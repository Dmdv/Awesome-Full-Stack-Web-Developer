#Uses python3

import sys

def get_max_number(arr_a):
    max_number = arr_a[0]
    for x in arr_a:
        """
        if (str(x)[0] > str(max_number)[0]):
            max_number = x
        elif(str(x)[0] == str(max_number)[0] and len(str(x)) == len (str(max_number))):
            for i in range(0, len(str(x))):
                if str(x)[i] > str(max_number)[i]:
                    max_number = x
                    break
        """
        if(int(str(x) + str(max_number)) > int(str(max_number) + str(x))):
            max_number = x
    return max_number

def largest_number(a):
    res = ""
    while len(a) > 0:
        largest_number = get_max_number(a)
        res += str(largest_number)
        a.remove(largest_number)
    return res

def test():
    print(largest_number([21, 3]))
    assert largest_number([21, 3]) == '321'

    print(largest_number([21, 24]))
    assert largest_number([21, 24]) == '2421'

    print(largest_number([2, 24]))
    assert largest_number([2, 24]) == '242'

    print(largest_number([1000, 5000, 21]))
    assert largest_number([1000, 5000, 21]) == '5000211000'

    print(largest_number([22, 224, 342]))
    assert(largest_number([22, 224, 342]) == '34222422')

    print(largest_number([1, 1, 1]))
    assert(largest_number([1, 1, 1]) == '111')

    print(largest_number([858, 85]))
    assert(largest_number([858, 85]) == '85885')

    print(largest_number([232, 23]))
    assert(largest_number([232, 23]) == '23232')

if __name__ == '__main__':
#    test()
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
