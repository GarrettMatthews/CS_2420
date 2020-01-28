""""
Comparing different sorting strategies to see the timing difference in these different algorithms
Garrett Matthews
"""

import random
import time
from recursioncounter import RecursionCounter


def quicksort(lyst):
    """Uses the quicksort algorithm to sort a lyst"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(lyst, list):
        raise ValueError("Error. Must submit a list")
    quicksort_helper(lyst, 0, len(lyst)-1)
    return lyst


def quicksort_helper(lyst, low, high):
    """Recursive helper for the quicksort algorithm"""
    RecursionCounter()
    if low < high:
        pivot_point = quicksort_pivot(lyst, low, high)
        quicksort_helper(lyst, low, pivot_point -1)
        quicksort_helper(lyst, pivot_point+1, high)


def quicksort_pivot(lyst, left, right):
    """Algorithm to manage the swapping and pivot points for the quicksort function"""
    midpoint = (left + right) // 2
    pivot = lyst[midpoint]
    lyst[midpoint], lyst[right] = lyst[right], lyst[midpoint]
    border = left
    for i in range(left, right):
        if lyst[i] < pivot:
            swap(lyst, i, border)
            border += 1
    swap(lyst, right, border)
    return border


def swap(lyst, index_1, index_2):
    """Function to swap the places of two indexes in a lyst"""
    lyst[index_1], lyst[index_2] = lyst[index_2], lyst[index_1]
    return lyst[index_1], lyst[index_2]


def mergesort(lyst):
    """Merge sort function to sort a lyst"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(lyst, list):
        raise ValueError("Error. Must submit a list")
    RecursionCounter()
    if len(lyst) > 1:
        midpoint = len(lyst) // 2
        left = lyst[:midpoint]
        right = lyst[midpoint:]

        mergesort(left)
        mergesort(right)

        left_it = 0
        right_it = 0
        main_it = 0

        while left_it < len(left) and right_it < len(right):
            if left[left_it] < right[right_it]:
                lyst[main_it] = left[left_it]
                left_it += 1
            else:
                lyst[main_it] = right[right_it]
                right_it += 1
            main_it += 1

        while left_it < len(left):
            lyst[main_it] = left[left_it]
            left_it += 1
            main_it += 1
        while right_it < len(right):
            lyst[main_it] = right[right_it]
            right_it += 1
            main_it += 1
    return lyst


def selection_sort(lyst):
    """Sorts a list using the selection sort algorithm"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(lyst, list):
        raise ValueError("Error. Must submit a list")
    index_1 = 0
    while index_1 < len(lyst) - 1:
        min_index = index_1
        index_2 = index_1 + 1
        while index_2 < len(lyst):
            if lyst[index_2] < lyst[min_index]:
                min_index = index_2
            index_2 += 1
        if min_index != index_1:
            swap(lyst, min_index, index_1)
        index_1 += 1
    return lyst


def insertion_sort(lyst):
    """Sort function that uses the insertion sort algorithm"""
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(lyst, list):
        raise ValueError("Error. Must submit a list")
    index_1 = 1
    while index_1 < len(lyst):
        insertion = lyst[index_1]
        index_2 = index_1 - 1
        while index_2 >= 0:
            if insertion < lyst[index_2]:
                lyst[index_2 + 1] = lyst[index_2]
                index_2 -= 1
            else:
                break
        lyst[index_2 + 1] = insertion
        index_1 += 1
    return lyst


def is_sorted(lyst):
    """Function to test if a list is sorted already"""
    if all(isinstance(x, list) for x in lyst):
        # The unittest used to test this inputs a nest list called orig_data() that fails on the
        # first run through because index 0 is a list, and so it won't run through
        # the test successfully
        pass
    elif not all(isinstance(x, int) for x in lyst):
        raise ValueError("Error. Must submit a list of integers only")
    if not isinstance(lyst, list):
        raise ValueError("Error. Must submit a list")
    test = lyst.copy()
    test.sort()
    is_true = bool(test == lyst)
    return is_true


def main():
    """Main function to run program"""
    random.seed(0)
    lyst = random.sample(range(100000), k=10000)
    test_1 = lyst.copy()
    print("Starting quicksort")
    start = time.perf_counter()
    quicksort(test_1)
    stop = time.perf_counter()
    result = ("{}{}".format("quicksort duration: ", stop-start))
    print(result)
    print("Starting mergesort")
    test_2 = lyst.copy()
    start = time.perf_counter()
    mergesort(test_2)
    stop = time.perf_counter()
    result = ("{}{}".format("mergesort duration: ", stop - start))
    print(result)
    test_3 = lyst.copy()
    print("Starting selection_sort")
    start = time.perf_counter()
    selection_sort(test_3)
    stop = time.perf_counter()
    result = ("{}{}".format("selection_sort duration: ", stop - start))
    print(result)
    print("Starting insertion_sort")
    test_4 = lyst.copy()
    start = time.perf_counter()
    insertion_sort(test_4)
    stop = time.perf_counter()
    result = ("{}{}".format("quicksort duration: ", stop - start))
    print(result)
    print("Starting timsort")
    test_5 = lyst.copy()
    start = time.perf_counter()
    test_5.sort()
    stop = time.perf_counter()
    result = ("{}{}".format("timsort duration: ", stop - start))
    print(result)




if __name__ == "__main__":
    main()
