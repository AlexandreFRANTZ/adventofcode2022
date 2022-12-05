#!/usr/bin/env python3

import sys

def main(argv):
    res = 0
    for i in open(argv[1], "r").read().split('\n'):
        poses = i.split(',')
        first = poses[0].split('-')
        second = poses[1].split('-')
        if (int(first[0]) >= int(second[0]) and int(second[1]) >= int(first[1])) or (int(second[0]) >= int(first[0]) and int(first[1]) >= int(second[1])):
            res+=1
    print(res)
    res = 0
    for i in open(argv[1], "r").read().split('\n'):
        poses = i.split(',')
        first = poses[0].split('-')
        second = poses[1].split('-')
        if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0])) or (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[0])):
            res+=1
    print(res)
    return 0

if __name__ == '__main__':
    main(sys.argv)