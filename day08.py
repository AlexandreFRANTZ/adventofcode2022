#!/usr/bin/env python3

import sys

def checkHigher(tab, x, y):
    cnt=0
    for i in range(0, x):
        if tab[i][y] >= tab[x][y]:
            cnt+=1
            break
    for i in range(x+1, len(tab)):
        if tab[i][y] >= tab[x][y]:
            cnt+=1
            break
    for i in range(0, y):
        if tab[x][i] >= tab[x][y]:
            cnt+=1
            break
    for i in range(y+1, len(tab[x])):
        if tab[x][i] >= tab[x][y]:
            cnt+=1
            break
    return False if cnt==4 else True

def checkHigher2(tab, x, y):
    res=1
    cnt=0
    if x != 0:
        for i in range(x-1, -1, -1):
            cnt+=1
            if tab[i][y] >= tab[x][y]:
                break
    res*=cnt
    cnt=0
    for i in range(x+1, len(tab)):
        cnt+=1
        if tab[i][y] >= tab[x][y]:
            break
    res*=cnt
    cnt=0
    if y != 0:
        for i in range(y-1, -1, -1):
            cnt+=1
            if tab[x][i] >= tab[x][y]:
                break
    res*=cnt
    cnt=0
    for i in range(y+1, len(tab[x])):
        cnt+=1
        if tab[x][i] >= tab[x][y]:
            break
    res*=cnt
    return res

def main(argv):
    tab = [[int(j) for j in i] for i in open(argv[1], "r").read().splitlines()]
    res = 0
    for x in range(len(tab)):
        for y in range(len(tab[x])):
            if checkHigher(tab, x, y):
                res+=1
    print(res)
    res = 0
    for x in range(len(tab)):
        for y in range(len(tab[x])):
            if (tmp:=checkHigher2(tab, x, y)) > res:
                res = tmp
    print(res)
    return 0

if __name__ == '__main__':
    main(sys.argv)