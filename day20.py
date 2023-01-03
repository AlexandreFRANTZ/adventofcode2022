#!/usr/bin/env python3

import sys

class Node:
    def __init__(self, data):
        self.data: int = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

class CircularLinkedList:
    def __init__(self):
        self.head: Node | None = None

    def print_list(self, starting_point=None):
        def traverse(self, starting_point: Node | None = None):
            if starting_point is None:
                starting_point = self.head
            node = starting_point
            while node is not None and (node.next != starting_point):
                yield node
                node = node.next
            yield node

        nodes = []
        for node in traverse(starting_point):
            nodes.append(str(node))
        print(", ".join(nodes))

def part_one(filename):
    sequence = read_input(filename)
    cll, nodes_ordered = initialize_cll(sequence)
    mix_numbers(nodes_ordered, cll)
    return sum(find_coords(cll, nodes_ordered[0]))

def part_two(filename):
    sequence = read_input(filename)
    cll, nodes_ordered = initialize_cll(sequence, 811589153)
    for _ in range(10):
        mix_numbers(nodes_ordered, cll)
    return sum(find_coords(cll, nodes_ordered[0]))

def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return list(map(int, f.read().splitlines()))

def initialize_cll(numbers, multiplier=1):
    sequence = [num * multiplier for num in numbers]
    cll = CircularLinkedList()
    cll.head = Node(sequence[0])
    prev_node = cll.head
    nodes_ordered: list[Node] = [cll.head]
    for i in range(1, len(sequence)):
        node = Node(sequence[i])
        prev_node.next = node
        node.prev = prev_node
        prev_node = node
        nodes_ordered.append(node)
    prev_node.next = cll.head
    cll.head.prev = prev_node
    return cll, nodes_ordered

def mix_numbers(nodes_ordered, cll):
    for node in nodes_ordered:
        steps = node.data % (len(nodes_ordered) - 1)
        if steps == 0:
            continue
        node.prev.next = node.next
        node.next.prev = node.prev
        if node == cll.head:
            cll.head = node.next
        insert_node = node
        for _ in range(steps):
            insert_node = insert_node.next
        node.prev = insert_node
        node.next = insert_node.next
        insert_node.next.prev = node
        insert_node.next = node

def find_coords(cll, node):
    coords = []
    node = cll.head
    while node.data != 0:
        node = node.next
    for ind in range(1, 3001):
        node = node.next
        if ind in [1000, 2000, 3000]:
            coords.append(node.data)
    return coords

def main(argv):
    print(part_one(argv[1]))
    print(part_two(argv[1]))

if __name__ == "__main__":
    main(sys.argv)