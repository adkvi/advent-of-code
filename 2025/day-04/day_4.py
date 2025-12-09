"""Advent of Code 2025 - Day 4: Count accessible paper rolls."""

def solve_part1():
    """Count rolls accessible by forklifts (< 4 adjacent rolls)."""
    with open('input.txt') as f:
        grid = [line.strip() for line in f.readlines()]
    
    rows, cols = len(grid), len(grid[0])
    return sum(sum(grid[r+dr][c+dc] == '@' for dr in [-1,0,1] for dc in [-1,0,1]
                   if (dr != 0 or dc != 0) and 0 <= r+dr < rows and 0 <= c+dc < cols) < 4
               for r in range(rows) for c in range(cols) if grid[r][c] == '@')

def solve_part2():
    """Count total rolls removed through iterative process."""
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    rows, cols, total = len(grid), len(grid[0]), 0
    while True:
        accessible = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '@'
                     and sum(grid[r+dr][c+dc] == '@' for dr in [-1,0,1] for dc in [-1,0,1]
                             if (dr != 0 or dc != 0) and 0 <= r+dr < rows and 0 <= c+dc < cols) < 4]
        if not accessible: break
        for r, c in accessible: grid[r][c] = '.'
        total += len(accessible)
    return total

if __name__ == "__main__": print("Part 1:", solve_part1()); print("Part 2:", solve_part2())

