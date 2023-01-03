#!/usr/bin/env python3

import sys
import operator
from typing import Any

def part_one(filename):
    monkeys = parse_input(filename)
    return int(calc_monkey_val("root", monkeys))

def parse_input(filename):
    with open(filename, encoding="utf-8") as f:
        monkeys: dict[str, int | str] = {
            line.strip().split(": ")[0]: line.strip().split(": ")[1]
            for line in f.readlines()
        }
    for monkey, val in monkeys.items():
        if isinstance(val, str) and len(val.split(" ")) == 1:
            monkeys[monkey] = int(val)
    return monkeys

def calc_monkey_val(monkey, monkeys):
    if isinstance(monkeys[monkey], str):
        m1, _, m2 = monkeys[monkey].split(" ")
        match monkeys[monkey].split(" ")[1]:
            case "+":
                operation = operator.add
            case "-":
                operation = operator.sub
            case "*":
                operation = operator.mul
            case "/":
                operation = operator.truediv
            case _:
                raise ValueError("Unknown operation")
        monkeys[monkey] = operation(
            calc_monkey_val(m1, monkeys), calc_monkey_val(m2, monkeys)
        )
    return monkeys[monkey]

def main(argv):
    print(part_one(argv[1]))

if __name__ == "__main__":
    main(sys.argv)