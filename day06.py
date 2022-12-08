#!/usr/bin/env python3

import sys

def algo(argv, mode):
    string = open(argv[1], "r").read()
    for ind, letter in enumerate(string):
        if ind < mode-1:
            continue
        strToCheck = ""
        for i in range(mode-1,-1, -1):
            strToCheck+=string[ind-i]
        one = 0
        for char in strToCheck:
            if strToCheck.count(char) != 1:
                one+=1
        if one == 0:
            return ind+1
    return 0

def main(argv):
    print(algo(argv, 4))
    print(algo(argv, 14))
    return 0

if __name__ == '__main__':
    main(sys.argv)