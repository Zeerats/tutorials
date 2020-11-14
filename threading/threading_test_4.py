### Threading example using the 'concurrent.futures' module and creating 3 threads (FutureObjects) manually.

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
    f1 = executor.submit(do_something, 1.5) # Creates a FutureObject and passes the function and arguments.
    f2 = executor.submit(do_something, 1.5)
    f3 = executor.submit(do_something, 1.5)
    print(f1.result()) # This will wait until the function completes and print the return statement (that's why the function needs a return statement).
    print(f2.result())
    print(f3.result())

# Sets a finishing point to later calculate total execution time.
finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s).') # Prints out total execution time by taking the rounded result of start and end time.
