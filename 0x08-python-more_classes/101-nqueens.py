#!/usr/bin/python3
"""
N-queens backtracking program puzzle.
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """checking if the queen doesn't exist already."""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """reject the solution or not."""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears answers in case of failure."""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """continuous backtracking until we find solution."""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)

    nqueens(0)
