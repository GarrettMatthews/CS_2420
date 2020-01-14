"""Python script to compare the speed of three different search algorithms"""
import random
from recursioncounter import RecursionCounter
import time
import math

def linear_search(lyst, target):
    """Function to run a linear search through a lyst, to find a target"""
    #if not isinstance(lyst, int):
    #    raise ValueError("List must be a list of integers")
    return target in lyst

def recursive_binary_search(lyst, target, low_index = 0, high_index = None):
    """Function to recursively search through a lyst by comparing its value with the midpoint"""
    #RecursionCounter()
    #if not isinstance(lyst, int):
    #    raise ValueError("List must be a list of integers")
    if high_index == None:
        high_index = len(lyst) -1
    midpoint = (lyst[low_index] + lyst[high_index]) // 2
    if low_index > high_index:
        return False
    elif midpoint == target:
        return True
    elif midpoint < target:
        return recursive_binary_search(lyst,target, midpoint - 1, high_index)
    elif midpoint > target:
        return recursive_binary_search(lyst,target, low_index, midpoint + 1)
    else:
        return False

def jump_search(lyst,target, search_index = 0):
    #if not isinstance(lyst, int):
    #    raise ValueError("List must be a list of integers")
    step = int(math.sqrt(len(lyst)))
    while search_index < len(lyst):
        if lyst[search_index] == target:
            return True
        else:
            return jump_search(lyst,target, min((search_index + step),(len(lyst)-1)))
    return False

def main():
    """Main function to run the progams"""
    print("Creating sorted array of 1000000")
    random.seed(0)
    #lyst = random.sample(range(100), k=10)
    lyst = list(range(100))
    lyst.sort()
    print("Finished creating sorted array of 1000000")
    #lin = linear_search(lyst, target = 10)
    #rec = recursive_binary_search(lyst, 10)
    jum = jump_search(lyst, 10)
    #print("Linear search results: ",lin)
    #print("Recursive search results: ", rec)
    print("Jump search results: ", jum)


if __name__ == "__main__":
    main()

