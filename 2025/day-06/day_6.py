"""Advent of Code 2025 - Day 6: Cephalopod Math Worksheet."""

def solve_part1():
    """Calculate grand total reading numbers horizontally (row-wise)."""
    with open('input.txt') as f: lines = f.read().strip().split('\n')
    grid, ops = [list(l) for l in lines[:-1]], lines[-1]
    
    problems, start = [], 0
    for c in range(len(grid[0]) + 1):
        if c == len(grid[0]) or all(grid[r][c] == ' ' for r in range(len(grid))):
            if c > start:
                nums = [int(''.join(grid[r][start:c]).strip()) for r in range(len(grid)) if ''.join(grid[r][start:c]).strip()]
                op = next((ch for ch in ops[start:c] if ch in '+*'), '+')
                problems.append((nums, op))
            start = c + 1
    
    return sum(sum(nums) if op == '+' else eval('*'.join(map(str, nums))) for nums, op in problems)

def solve_part2():
    """Calculate grand total reading numbers vertically (column-wise)."""
    with open('input.txt') as f: lines = f.read().strip().split('\n')
    grid, ops = [list(l) for l in lines[:-1]], lines[-1]
    
    problems, start = [], 0
    for c in range(len(grid[0]) + 1):
        if c == len(grid[0]) or all(grid[r][c] == ' ' for r in range(len(grid))):
            if c > start:
                # Read vertically: each column becomes a number
                nums = [int(''.join(grid[r][col] for r in range(len(grid)) if grid[r][col] != ' ')) 
                       for col in range(start, c) if any(grid[r][col] != ' ' for r in range(len(grid)))]
                op = next((ch for ch in ops[start:c] if ch in '+*'), '+')
                problems.append((nums, op))
            start = c + 1
    
    return sum(sum(nums) if op == '+' else eval('*'.join(map(str, nums))) for nums, op in problems)

if __name__ == "__main__": print("Part 1:", solve_part1()); print("Part 2:", solve_part2())
