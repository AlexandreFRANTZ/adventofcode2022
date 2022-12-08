#!/usr/bin/env python3
from collections import defaultdict
from itertools import accumulate
import sys

def main(argv):
    dirs = defaultdict(int)
    for line in open(argv[1], "r").read().splitlines():
        match line.split():
            case "$", "cd", "/":
                path = ["/"]
            case "$", "cd", "..":
                path.pop()
            case "$", "cd", dir:
                path.append(dir + "/")
            case "$" | "dir", *_:
                continue
            case size, _:
                for p in accumulate(path):
                    dirs[p] += int(size)
    print(sum(size for size in dirs.values() if size <= 100000))
    print(min(size for size in dirs.values() if size >= dirs["/"] - 40_000_000))

if __name__ == "__main__":
    main(sys.argv)