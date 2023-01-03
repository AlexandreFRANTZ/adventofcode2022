#!/usr/bin/env python3

import sys

def getLineToDigit(line):
    result = 0
    for char in line:
        match char:
            case "2":
                result = result * 5 + 2
            case "1":
                result = result * 5 + 1
            case "0":
                result = result * 5
            case "-":
                result = result * 5 - 1
            case "=":
                result = result * 5 - 2
    return result

def transformDecimal(result):
    resStr = ""
    while result:
        tmp = result % 5
        result = result // 5
        if tmp > 2:
            tmp -= 5
            result+=1
        match tmp:
            case 2:
                resStr = "2" + resStr
            case 1:
                resStr = "1" + resStr
            case 0:
                resStr = "0" + resStr
            case -1:
                resStr = "-" + resStr
            case -2:
                resStr = "=" + resStr
    return resStr

def part_one(filename):
    result = 0
    for line in open(filename, "r").read().splitlines():
        result+=getLineToDigit(line)
    return result

def main(argv):
    print(transformDecimal(part_one(argv[1])))

if __name__ == "__main__":
    main(sys.argv)