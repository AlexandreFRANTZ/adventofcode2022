#!/usr/bin/env python3

import sys

def main(argv):
    lines = open(argv[1], "r").read().split("\n")
    lineCnt = 0
    stcks = []
    for line in lines:
        if line == "":
            break
        nodes = [line[i:i+4] for i in range(0, len(line), 4)]
        stcks.append(nodes)
        lineCnt+=1
    stcks.pop()
    stacks = [[] for _ in range(len(stcks[0]))]
    for stck in stcks:
        for x, stckNode in enumerate(stck):
            if stckNode[1] != ' ':
                stacks[x].insert(0, stckNode[1])
    commands = [lines[i] for i in range(lineCnt+1, len(lines))]

    for command in commands:
        nb = int(command.split(' ')[1])
        first = int(command.split(' ')[3])
        second = int(command.split(' ')[5])
        for i in range(nb):
            stacks[second-1].append(stacks[first-1].pop())
    res = ""
    for stack in stacks:
        res+=stack[len(stack)-1]
    print(res)

    stacks = [[] for _ in range(len(stcks[0]))]
    for stck in stcks:
        for x, stckNode in enumerate(stck):
            if stckNode[1] != ' ':
                stacks[x].insert(0, stckNode[1])
    commands = [lines[i] for i in range(lineCnt+1, len(lines))]
    for command in commands:
        nb = int(command.split(' ')[1])
        first = int(command.split(' ')[3])
        second = int(command.split(' ')[5])
        toAppend = []
        for i in range(nb):
            toAppend.append(stacks[first-1].pop())
        toAppend.reverse()
        for node in toAppend:
            stacks[second-1].append(node)
    res = ""
    for stack in stacks:
        res+=stack[len(stack)-1]
    print(res)
    return 0

if __name__ == '__main__':
    main(sys.argv)