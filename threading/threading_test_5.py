### Threading example using the 'concurrent.futures' module and creating 10 threads (FutureObjects) using a list comprehension loop.

import concurrent.futures
import time


# Sets a starting point to later calculate total execution time.
start = time.perf_counter()

# Now the function takes an argument for the seconds. This will be handled and passed when the threads are created, using the 'args' argument.
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done sleeping.' # Changed to a return statement so we can use it with the FutureObject.

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1.5) for _ in range(10)] # Creates a list of FutureObjects and passes the function and arguments.

    # Yields the results of the threads as the complete.
    for f in concurrent.futures.as_completed(results):
        print(f.result())

# Sets a finishing point to later calculate total execution time.
finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s).') # Prints out total execution time by taking the rounded result of start and end time.
