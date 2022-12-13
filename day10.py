#!/usr/bin/env python3

import sys

def addChar(position, toPlace):
    if (toPlace == position or toPlace == position-1 or toPlace == position+1):
        return '#'
    return '.'

def main(argv):
    cycle = 1
    cycle2 = 1
    result = 1
    results = []
    toAdd = []
    passed = False
    string = "#"
    for command in open(argv[1], "r").read().splitlines():
        passed = False
        cmd = command.split(' ')
        if toAdd:
            result+=toAdd.pop(0)
            string+=addChar(result, cycle2)
            cycle+=1
            cycle2+=1
            if (cycle%40==20 and cycle!=0) or cycle==20:
                results.append(result)
                passed = True
        if (cycle2%41==0):
            cycle2 = 1
        if cmd[0] == "addx":
            toAdd.append(int(cmd[1]))
            string+=addChar(result, cycle2)
            cycle+=1
            cycle2+=1
        elif cmd[0] == "noop":
            string+=addChar(result, cycle2)
            cycle+=1
            cycle2+=1
        if (cycle2%41==0):
            cycle2 = 1
        if passed == False:
            if (cycle%40==20 and cycle!=0) or cycle == 20:
                results.append(result)
    finalRes = 0
    addi = 20
    for i, res in enumerate(results):
        if ((addi + (40 * i)) > 220):
            break
        finalRes += abs(res) * (addi + (40 * i))
    print(finalRes)
    for i, c in enumerate(string):
        if (i%40==0):
            print("")
        print(c, end='')
    print("")
    return 0

if __name__ == '__main__':
    main(sys.argv)