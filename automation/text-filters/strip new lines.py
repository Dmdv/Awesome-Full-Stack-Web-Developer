#!/usr/local/bin/python3

import fileinput

txt = []

if __name__ == "__main__":
    for line in fileinput.input():
        tmp = line.split()
        txt.append(''.join(tmp))

print(''.join(txt))