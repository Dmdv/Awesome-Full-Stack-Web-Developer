#!/usr/local/bin/python3
# coding=utf-8

import fileinput

def uniquelines(lineslist):
    unique = {}
    result = []
    for item in lineslist:
        if item.strip() in unique: continue
        unique[item.strip()] = 1
        result.append(item)
    return result

if __name__ == "__main__":
    lines = uniquelines(fileinput.input())

    for line in lines:
        tmp = line.strip()
        print(''.join(tmp))
