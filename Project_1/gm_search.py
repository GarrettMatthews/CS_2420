"""Python script to compare the speed of three different search algorithms"""
import random
from recursioncounter import RecursionCounter
import time
import math


def linear_search(lyst, target):
    """Function to run a linear search through a lyst, to find a target"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(target, int):
        raise ValueError("Error. Target must be an integer")
    return target in lyst

def recursive_binary_search(lyst,target):
    """Function to call the recursive binary search function"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(target, int):
        raise ValueError("Error. Target must be an integer")
    return recursive_binary_search_helper(lyst,target)


def recursive_binary_search_helper(lyst, target, low_index = 0, high_index = None):
    """Function to recursively search through a lyst by comparing its value with the midpoint"""
    RecursionCounter()
    if high_index == None:
        high_index = len(lyst) - 1
    midpoint = (low_index + high_index) // 2
    if low_index > high_index:
        return False
    elif lyst[low_index] == target:
        return True
    elif lyst[high_index] == target:
        return True
    elif low_index + 2 == high_index:
        return False
    elif lyst[midpoint] == target:
        return True
    elif lyst[midpoint] < target:
        return recursive_binary_search(lyst, target, midpoint - 1, high_index)
    elif lyst[midpoint] > target:
        return recursive_binary_search(lyst, target, low_index, midpoint + 1)
    else:
        return False


def jump_search(lyst,target, start = 0):
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(target, int):
        raise ValueError("Error. Target must be an integer")
    step = int(math.sqrt(len(lyst)))
    end = start + step
    temp = lyst[start:min(len(lyst),end)]
    if target in temp:
        return True
    else:
        return jump_search(lyst,target, start + step)
    return False


def main():
    """Main function to run the progams"""
    print("Creating sorted array of 1000000")
    random.seed(0)
    lyst = random.sample(range(100000000000), k=100000)
    #lyst = list(range(100))
    lyst.sort()
    print("Finished creating sorted array of 1000000")
    lin = linear_search(lyst,lyst[0])
    rec = recursive_binary_search(lyst, lyst[-1])
    jum = jump_search(lyst, lyst[5])
    print("Linear search results: ",lin)
    print("Recursive search results: ", rec)
    print("Jump search results: ", jum)



if __name__ == "__main__":
    main()

