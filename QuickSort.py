import random
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(5000)
# ----------------------

# Randomized Quicksort

# ----------------------

def randomized_quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    equal = [x for i, x in enumerate(arr) if x == pivot]
    greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# ----------------------

# Deterministic Quicksort (first element as pivot)

# ----------------------

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# ----------------------

# Generate Test Arrays

# ----------------------

def generate_test_cases(n):

    return {
        "Random": [random.randint(0, 10000) for _ in range(n)],
        "Sorted": list(range(n)),
        "Reversed": list(range(n, 0, -1)),
        "Repeated": [5] * n
    }

# ----------------------

# Benchmarking

# ----------------------

def benchmark_sorts(sizes):

    results = {"Randomized": [], "Deterministic": []}

    for n in sizes:
        test_cases = generate_test_cases(n)
        randomized_times = []
        deterministic_times = []
        for key, arr in test_cases.items():
            arr_copy = arr[:]
            start = time.time()
            randomized_quicksort(arr_copy)
            randomized_times.append(time.time() - start)
            arr_copy = arr[:]
            start = time.time()
            deterministic_quicksort(arr_copy)
            deterministic_times.append(time.time() - start)

        results["Randomized"].append(np.mean(randomized_times))

        results["Deterministic"].append(np.mean(deterministic_times))

    return results

# ----------------------

# Run Benchmark

# ----------------------

sizes = [100, 500, 1000, 2000]

results = benchmark_sorts(sizes)

# Plotting the results

plt.plot(sizes, results["Randomized"], label="Randomized Quicksort", marker='o')

plt.plot(sizes, results["Deterministic"], label="Deterministic Quicksort", marker='x')

plt.xlabel("Input Size (n)")

plt.ylabel("Average Time (s)")

plt.title("Quicksort Performance Comparison")

plt.legend()

plt.grid(True)

plt.show()
 
