"""Advent of Code 2025 - Day 3: Find max joltage from battery banks."""

def solve_part1():
    """Find max 2-digit number from each bank by selecting any two batteries."""
    with open('input.txt') as f:
        return sum(max(int(line[i] + line[j]) for i in range(len(line)) 
                      for j in range(i+1, len(line))) for line in f.read().strip().split('\n'))

def solve_part2():
    """Find max 12-digit number from each bank by selecting exactly 12 batteries."""
    with open('input.txt') as f:
        total = 0
        for line in f.read().strip().split('\n'):
            stack, rem = [], len(line) - 12
            for d in line:
                while stack and stack[-1] < d and rem > 0: stack.pop(); rem -= 1
                stack.append(d)
            total += int(''.join(stack[:12]))
        return total

if __name__ == "__main__": print("Part 1:", solve_part1()); print("Part 2:", solve_part2())
