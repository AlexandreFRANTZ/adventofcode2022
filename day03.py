#!/usr/bin/env python3

import sys

def main(argv):
    lst = []
    res = 0
    for elem in open(argv[1], "r").read().split('\n'):
        first = elem[slice(0, len(elem)//2)]
        second = elem[slice(len(elem)//2, len(elem))]
        lst.append(set(first).intersection(set(second)))
    for char in lst:
        asciiChar = ord(str(char.pop()))
        if asciiChar >= 97:
            res+=asciiChar-96
        else:
            res+=asciiChar-64+26
    print(res)
    lst = []
    res = 0
    firstGrp = 0
    first = []
    for elem in open(argv[1], "r").read().split('\n'):
        if firstGrp < 3:
            first.append(elem)
            firstGrp+=1
            if firstGrp == 3:
                lst.append((set(first[0]).intersection(set(first[1]))).intersection(set(first[2])))
                first = []
                firstGrp=0
    for char in lst:
        asciiChar = ord(str(char.pop()))
        if asciiChar >= 97:
            res+=asciiChar-96
        else:
            res+=asciiChar-64+26
    print(res)
    return 0

if __name__ == '__main__':
    main(sys.argv)