import random
import matplotlib.pyplot as plt
import time

def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(arr):
    element_counts = {}
    for num in arr:
        element_counts[num] = element_counts.get(num, 0) + 1

    unique_elements = [num for num, count in element_counts.items() if count == 1]
    non_unique_elements = [num for num, count in element_counts.items() if count > 1]

    return len(arr) == len(set(arr)), unique_elements, non_unique_elements

def measure_execution_time(n_values, max_value, repetitions, seed):
    worst_cases = []
    average_cases = []

    for n in n_values:
        times = []

        for _ in range(repetitions):
            arr = generate_array(n, max_value, seed)
            start_time = time.perf_counter()
            result, unique_elements, non_unique_elements = is_unique(arr)
            end_time = time.perf_counter()
            times.append(end_time - start_time)

            # menampilkan elemen unik dan tidak unik
            if _ == 0:
                print(f"Array size: {n}")
                print(f"Unique elements: {unique_elements}")
                print(f"Non-unique elements: {non_unique_elements}\n")

        # menghitung waktu eksekusi worst dan average case
        worst_cases.append(max(times))
        average_cases.append(sum(times) / repetitions)

    return worst_cases, average_cases

# Parameter
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 152
repetitions = 10
seed = 42

worst_cases, average_cases = measure_execution_time(n_values, max_value, repetitions, seed)

# menampilkam waktu eksekusi worst dan average case
print("\nExecution Times:")
print(f"{'n':<10}{'Worst Case (s)':<20}{'Average Case (s)'}")
for n, wc, ac in zip(n_values, worst_cases, average_cases):
    print(f"{n:<10}{wc:<20.6f}{ac:.6f}")

# untuk graphnya
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_cases, label='Worst Case', marker='o', color='r')
plt.plot(n_values, average_cases, label='Average Case', marker='o', color='b')
plt.title("Worst Case vs Average Case Execution Times")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid()
plt.show()
