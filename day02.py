#!/usr/bin/env python3

import sys

def main(argv):
    res = 0
    for i in open(argv[1], "r").read().split('\n'):
        us = i.split(' ')
        him = us[0]
        me = us[1]
        if (him == 'A'):
            if (me == 'X'):
                res+=1+3
            if (me == 'Y'):
                res+=2+6
            if (me == 'Z'):
                res+=3+0
        if (him == 'B'):
            if (me == 'X'):
                res+=1+0
            if (me == 'Y'):
                res+=2+3
            if (me == 'Z'):
                res+=3+6
        if (him == 'C'):
            if (me == 'X'):
                res+=1+6
            if (me == 'Y'):
                res+=2+0
            if (me == 'Z'):
                res+=3+3
    print(res)
    res = 0
    for i in open(argv[1], "r").read().split('\n'):
        us = i.split(' ')
        him = us[0]
        me = us[1]
        if (him == 'A'):
            if (me == 'X'):
                res+=3+0
            if (me == 'Y'):
                res+=1+3
            if (me == 'Z'):
                res+=2+6
        if (him == 'B'):
            if (me == 'X'):
                res+=1+0
            if (me == 'Y'):
                res+=2+3
            if (me == 'Z'):
                res+=3+6
        if (him == 'C'):
            if (me == 'X'):
                res+=2+0
            if (me == 'Y'):
                res+=3+3
            if (me == 'Z'):
                res+=1+6
    print(res)
    return 0

if __name__ == '__main__':
    main(sys.argv)