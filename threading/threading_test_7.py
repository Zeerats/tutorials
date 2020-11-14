### Threading example using the 'concurrent.futures' module and creating 5 threads (FutureObjects).
# The FutureObjects will have different arguments passed from a list (using a 'map' function) and the results will be yielded once everything is finished and in order of execution.

import concurrent.futures
import time


# Sets a starting point to later calculate total execution time.
start = time.perf_counter()

# Now the function takes an argument for the seconds. This will be handled and passed when the threads are created, using the 'args' argument.
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s).' # Changed to a return statement so we can use it with the FutureObject.

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1] # Creates a list for different sleep times of the functions that will be added to the pool.
    results = executor.map(do_something, secs) # Maps the arguments to the function and passes these to the executor.

    for result in results:
        print(result) # The results are printed in the order that they were started (because of the 'map function').

# Sets a finishing point to later calculate total execution time.
finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s).') # Prints out total execution time by taking the rounded result of start and end time.

# The functions take only 5 seconds to finish, even though the total seconds are 15.
# All threads are started almost at the same time, but results are yielded when all of them finished and in order of execution.
