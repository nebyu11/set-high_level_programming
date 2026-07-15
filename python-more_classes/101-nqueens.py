#!/usr/bin/python3
"""N-Queens puzzle solver."""
import sys


def solve(n, row, queens, solutions):
    """Recursively solve the N-Queens puzzle using backtracking.
    Args:
        n (int): Size of board.
        row (int): Current row.
        queens (list): Placed queens coordinates list [[r, c], ...].
        solutions (list): List of all solutions.
    """
    if row == n:
        solutions.append(queens.copy())
        return

    for col in range(n):
        # Check if placement is safe
        safe = True
        for q_row, q_col in queens:
            if q_col == col or abs(q_row - row) == abs(q_col - col):
                safe = False
                break
        if safe:
            queens.append([row, col])
            solve(n, row + 1, queens, solutions)
            queens.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, [], solutions)
    for sol in solutions:
        print(sol)
