"""
File: fib.py
Project 3.6
File says 3.5, but I didn't do anything on that one that was worth saving, so I'm stealing it for 3.6
Employs memoization to improve the efficiency of recursive Fibonacci.
"""

def fib(n, table):
    """Fibonacci function with a table for memoization."""
    if n < 3:
        return 1
    else:
        if (n-1) in table:
            return table[n-1]
        if (n-2) in table:
            return table[n-2]
        else:
            table[n-1] = fib(n-1, table)
            table[n-2] = fib(n - 2, table)
        return fib(n-1, table) + fib(n-2,table)


def main():
    """Tests the function with some powers of 2."""
    problemSize = 2
    print("%4s%12s" % ("n", "fib"))
    for count in range(5):
        print("%4d%12d" % (problemSize, fib(problemSize, {})))
        problemSize *= 2


if __name__ == "__main__":
    main()
