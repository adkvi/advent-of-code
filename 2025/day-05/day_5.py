"""Advent of Code 2025 - Day 5: Count fresh ingredient IDs."""

def solve_part1():
    """Count available ingredient IDs that are fresh."""
    with open('input.txt') as f:
        ranges_text, ids_text = f.read().strip().split('\n\n')
    
    ranges = [tuple(map(int, line.split('-'))) for line in ranges_text.split('\n')]
    available_ids = [int(line) for line in ids_text.split('\n')]
    
    return sum(any(start <= id_num <= end for start, end in ranges) for id_num in available_ids)

def solve_part2():
    """Count total ingredient IDs considered fresh by merging ranges."""
    with open('input.txt') as f:
        ranges_text = f.read().strip().split('\n\n')[0]
    
    ranges = sorted(tuple(map(int, line.split('-'))) for line in ranges_text.split('\n'))
    
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return sum(end - start + 1 for start, end in merged)

if __name__ == "__main__": print("Part 1:", solve_part1()); print("Part 2:", solve_part2())

