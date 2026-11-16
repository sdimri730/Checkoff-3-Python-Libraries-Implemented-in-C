import time
#numpy must be installed in order to run this program, the rest can be run if Python is installed
import numpy as np

def test():
    #initialize Python List for testing
    py_list = [0] * 1000000

    # 1. Capture the start time right before the operation
    start_time_python = time.perf_counter()
    # --- Run the operation you want to test ---
    result = [x + 1 for x in py_list]

    # 2. Capture the end time right after it finishes
    end_time_python = time.perf_counter()

    # 3. Calculate elapsed time
    elapsed_duration = end_time_python - start_time_python
    print(f"Python List: Operation took {elapsed_duration:.4f} seconds")

    #initialize numpy array for testing
    np_array = np.zeros(1000000)

    # 1. Capture the start time right before the operation
    start_time_np = time.perf_counter()
    # --- Run the operation you want to test ---
    np_result = np_array + 1

    # 2. Capture the end time right after it finishes
    end_time_np = time.perf_counter()

    # 3. Calculate elapsed time
    elapsed_duration = end_time_np - start_time_np
    print(f"NumPy Array: Operation took {elapsed_duration:.4f} seconds")
    print()


for i in range(10):
    test()
