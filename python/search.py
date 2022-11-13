#!/usr/bin/env python3

import random
import time

def binary_search_rec(arr, key):
    def __binary_search_rec(arr, low, high, key):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return __binary_search_rec(arr, low, mid - 1, key)
            else:
                return __binary_search_rec(arr, mid + 1, high, key)
        else:
            return -1
    return __binary_search_rec(arr, 0, len(arr) - 1, key)

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while high >= low:
        mid = (low + high) // 2
        if(arr[mid] == key):
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
 
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while high >= low and key >= arr[low] and key <= arr[high]:
        mid = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if(arr[mid] == key):
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [random.randint(0, 10000000) for i in range(1000000)]
arr.sort()
keys = [arr[random.randint(0, 1000000)] for i in range(10)]
keys.extend(random.randint(0, 1000000)  for i in range(5))

# TODO: benchmark linear search, binary search, and interpolation search for the given keys
for key in keys:
    start = time.perf_counter_ns()
    found = linear_search(arr, key)
    end = time.perf_counter_ns()
    print(f"Time Linear: {end-start} ns")

    start = time.perf_counter_ns()
    found = binary_search_rec(arr, key)
    end = time.perf_counter_ns()
    print(f"Time Binary Rec: {end-start} ns")

    start = time.perf_counter_ns()
    found = interpolation_search(arr, key)
    end = time.perf_counter_ns()
    print(f"Time Interpolation: {end-start} ns")

    start = time.perf_counter_ns()
    found = binary_search(arr, key)
    end = time.perf_counter_ns()
    print(f"Time Binary It: {end-start} ns")
