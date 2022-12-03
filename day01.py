#!/usr/bin/env python3

import sys

def main(argv):
    intList = []
    intToList = 0
    for i in open(argv[1], "r").read().split('\n'):
        if (not(i)):
            intList.append(intToList)
            intToList = 0
        else:
            intToList+=int(i)
    print(max(intList))
    intList.sort()
    intList.reverse()
    print(intList[0] + intList[1] + intList[2])
    return 0

if __name__ == '__main__':
    main(sys.argv)