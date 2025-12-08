"""Advent of Code 2025 - Day 2: Find sum of invalid product IDs."""

def solve_part1():
    """Find sum of numbers made of digits repeated exactly twice."""
    with open('input.txt') as f:
        ranges = [(int(a), int(b)) for line in f.read().split(',') 
                  for a, b in [line.strip().split('-')]]
    
    return sum(doubled for start, end in ranges
               for digits in range(1, len(str(end)) // 2 + 2)
               for half in range(1 if digits == 1 else 10**(digits-1), 10**digits)
               for doubled in [half * (10**digits + 1)]
               if start <= doubled <= end)

def solve_part2():
    """Find sum of numbers made of digits repeated at least twice."""
    with open('input.txt') as f:
        ranges = [(int(a), int(b)) for line in f.read().split(',') 
                  for a, b in [line.strip().split('-')]]
    
    return sum(set(repeated for pattern_len in range(1, max(len(str(end)) for _, end in ranges) // 2 + 1)
                   for pattern in range(1 if pattern_len == 1 else 10**(pattern_len-1), 10**pattern_len)
                   for reps in range(2, max(len(str(end)) for _, end in ranges) // pattern_len + 1)
                   for repeated in [int(str(pattern) * reps)]
                   for start, end in ranges if start <= repeated <= end))

if __name__ == "__main__": 
    print("Part 1:", solve_part1())
    print("Part 2:", solve_part2())
