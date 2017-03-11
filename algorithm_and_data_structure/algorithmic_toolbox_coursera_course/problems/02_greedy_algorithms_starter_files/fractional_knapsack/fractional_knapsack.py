# Uses python3
import sys

def sort_lists_by(lists, key_list=0, desc=True):
    return zip(*sorted(zip(*lists), reverse=desc, key=lambda x: x[key_list]))

def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_unit = []
    for i in range(0, len(weights)):
        value_per_unit.append( values[i] / weights [i])

    vpu_s, values_s, weights_s = sort_lists_by([value_per_unit, values, weights])
    current_index = 0

    while capacity > 0:
        if (weights_s[current_index] < capacity):
            value += values_s[current_index]
            capacity -= weights_s[current_index]
        else:
            weight_precentage = capacity / weights_s[current_index]
            value += weight_precentage * values_s[current_index]
            capacity -= weight_precentage * weights_s[current_index]

        if(current_index < len(weights_s) - 1):
            current_index += 1
        else:
            break;

    return value

def test_optimal_value():
    capacity = 1000
    values = [500]
    weights = [30]
    opt_value = get_optimal_value(capacity, weights, values)
    print(opt_value)

    capacity = 10 
    values = [500]
    weights = [30]
    opt_value = get_optimal_value(capacity, weights, values)
    print(opt_value)

    capacity = 50
    values = [60, 100, 120]
    weights = [20, 50, 30]
    opt_value = get_optimal_value(capacity, weights, values)
    print(opt_value)

if __name__ == "__main__":

   #  test_optimal_value()

    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
