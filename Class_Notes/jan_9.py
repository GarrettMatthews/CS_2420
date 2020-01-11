"""Class notes for January 9, 2020"""

def factorial(fac):
    """Program that calculates the factorial of a value x"""
    if not isinstance(fac, int):
        raise ValueError("x must be an integer")
    if fac < 0:
        raise ValueError("x must be non-negative")
    #Base case
    if fac <= 1:
        return 1
    # recursive case
    return fac * (factorial(fac - 1))


def main():
    """Main function to run other functions"""
    try:
        print(factorial(6))
    except ValueError as err:
        print("Oops", err)

# __ == 'dunder' (double under) #

if __name__ == "__main__":
    main()
""" 
For project 1:
Sequential search- 
    you can use *in* - like (return target in lyst)
Midpoint search tip: 
    midpoint_search(lyst, target, low_index = 0, high_index = None)
    Validate lyst and target, then
    if high_index is None
        hi = len(lyst)-1
    midpoint = (low + high) // 2
    if target is < mid, do mid -1. if target is > mid, do mid + 1
        **Base cases** if midpoint is first target, or if hi and low become inverted
Jump search:
    Searching chunks for the number
    Most efficient(?) len(lyst)**1/2
    min(len(lyst)-1, <last index of chunk>) to control for accidentally searching past the last index of the list
    
This project is more for setting up the IDE and figuring out how to run unittests 
"""