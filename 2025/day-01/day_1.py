"""Advent of Code 2025 - Day 1: Count times dial points to position 0."""

def solve_part1():
    """Count zero hits after each rotation."""
    with open('input.txt') as f:
        rotations = f.read().strip().split('\n')
    
    position, zero_count = 50, 0
    for rotation in rotations:
        position = (position + (-1 if rotation[0] == 'L' else 1) * int(rotation[1:])) % 100
        zero_count += position == 0
    return zero_count

def solve_part2():
    """Count zero hits during and after each rotation."""
    with open('input.txt') as f:
        rotations = f.read().strip().split('\n')
    
    position, zero_count = 50, 0
    for rotation in rotations:
        direction = -1 if rotation[0] == 'L' else 1
        for _ in range(int(rotation[1:])):
            position = (position + direction) % 100
            zero_count += position == 0
    return zero_count

if __name__ == "__main__": 
    print("Part 1:", solve_part1())
    print("Part 2:", solve_part2())
