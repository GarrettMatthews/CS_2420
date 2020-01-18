"""
Python script to compare the speed of three different search algorithms
Garrett Matthews
"""

import random
import time
import math
from recursioncounter import RecursionCounter




def linear_search(lyst, target):
    """Function to run a linear search through a lyst, to find a target"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(target, int):
        raise ValueError("Error. Target must be an integer")
    for i in lyst:
        if i == target:
            return True
    return False


def recursive_binary_search(lyst, target):
    """Function to call the recursive binary search function"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(target, int):
        raise ValueError("Error. Target must be an integer")
    return recursive_binary_search_helper(lyst, target)


def recursive_binary_search_helper(lyst, target, low_index=0, high_index=None):
    """Function to recursively search through a lyst by comparing its value with the midpoint"""
    RecursionCounter()
    if high_index is None:
        high_index = len(lyst) - 1
    midpoint = (low_index + high_index) // 2
    if low_index > high_index:
        return False
    elif midpoint + 1 == high_index:
        return False
    elif midpoint - 1 == low_index:
        if lyst[low_index] == target:
            return True
        elif lyst[high_index] == target:
            return True
        else:
            return False
    elif lyst[midpoint] == target:
        return True
    elif lyst[midpoint] < target:
        return recursive_binary_search_helper(lyst, target, midpoint - 1, high_index)
    elif lyst[midpoint] > target:
        return recursive_binary_search_helper(lyst, target, low_index, midpoint + 1)
    else:
        return False


def jump_search(lyst, target, start=0):
    """Function to search chunks of a list, the chunk being equal to the
    square root of the list length"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(target, int):
        raise ValueError("Error. Target must be an integer")
    step = int(math.sqrt(len(lyst)))
    while start < len(lyst):
        if lyst[start] == target:
            return True
        elif lyst[start] > target:
            temp = lyst[(start - step): start]
            if target in temp:
                return True
            else:
                return False
        start += step
    if target == lyst[-1]:
        return True
    return False


def pnt_format(per_time, search_type, result):
    """Function to control the format of the result print statement"""
    if search_type == "linear":
        statement = ("{}{}{}{}{}{}{}".format('\t', "linear_search() returned ", result, " in ",
                                             per_time, " seconds", '\n'))
    elif search_type == "binary":
        statement = ("{}{}{}{}{}{}{}".format('\t', "recursive_binary_search() returned ",
                                             result, " in ", per_time, " seconds", '\n'))
    elif search_type == "jump":
        statement = ("{}{}{}{}{}{}{}".format('\t', "jump_search() returned ", result, " in ",
                                             per_time, " seconds", '\n'))
    else:
        statement = "Error with inputted type"
    return statement



def main():
    """Main function to run the program"""
    print("Creating sorted array of 1000000")
    random.seed(0)
    lyst = random.sample(range(100000000000), k=1000000)
    lyst.sort()
    print("Finished creating sorted array of 1000000")
    lin_1 = ("{}{}{}".format('\n', "Searching for a number at the beginning of the array", '\n'))
    print(lin_1)
    start_1 = time.perf_counter()
    lin = linear_search(lyst, lyst[0])
    stop_1 = time.perf_counter()
    print(pnt_format((stop_1-start_1), "linear", lin))
    start_2 = time.perf_counter()
    rec = recursive_binary_search(lyst, lyst[0])
    stop_2 = time.perf_counter()
    print(pnt_format((stop_2 - start_2), "binary", rec))
    start_3 = time.perf_counter()
    jum = jump_search(lyst, lyst[0])
    stop_3 = time.perf_counter()
    print(pnt_format((stop_3 - start_3), "jump", jum))
    lin_2 = ("{}{}{}".format('\n', "Searching for a number near the middle of the array", '\n'))
    print(lin_2)
    start_1 = time.perf_counter()
    lin = linear_search(lyst, lyst[500000])
    stop_1 = time.perf_counter()
    print(pnt_format((stop_1 - start_1), "linear", lin))
    start_2 = time.perf_counter()
    rec = recursive_binary_search(lyst, lyst[500000])
    stop_2 = time.perf_counter()
    print(pnt_format((stop_2 - start_2), "binary", rec))
    start_3 = time.perf_counter()
    jum = jump_search(lyst, lyst[500000])
    stop_3 = time.perf_counter()
    print(pnt_format((stop_3 - start_3), "jump", jum))
    lin_3 = ("{}{}{}".format('\n', "Searching for a number near the end of the array", '\n'))
    print(lin_3)
    start_1 = time.perf_counter()
    lin = linear_search(lyst, lyst[-1])
    stop_1 = time.perf_counter()
    print(pnt_format((stop_1 - start_1), "linear", lin))
    start_2 = time.perf_counter()
    rec = recursive_binary_search(lyst, lyst[-1])
    stop_2 = time.perf_counter()
    print(pnt_format((stop_2 - start_2), "binary", rec))
    start_3 = time.perf_counter()
    jum = jump_search(lyst, lyst[-1])
    stop_3 = time.perf_counter()
    print(pnt_format((stop_3 - start_3), "jump", jum))
    lin_4 = ("{}{}{}".format('\n', "Searching for a number NOT in the array", '\n'))
    print(lin_4)
    start_1 = time.perf_counter()
    lin = linear_search(lyst, -1)
    stop_1 = time.perf_counter()
    print(pnt_format((stop_1 - start_1), "linear", lin))
    start_2 = time.perf_counter()
    rec = recursive_binary_search(lyst, -1)
    stop_2 = time.perf_counter()
    print(pnt_format((stop_2 - start_2), "binary", rec))
    start_3 = time.perf_counter()
    jum = jump_search(lyst, -1)
    stop_3 = time.perf_counter()
    print(pnt_format((stop_3 - start_3), "jump", jum))

if __name__ == "__main__":
    main()
