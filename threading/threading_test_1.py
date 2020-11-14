### Threading example using the 'threading' module and creating each thread separately.

import threading
import time


# Sets a starting point to later calculate total execution time.
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping.')


# The function will be run three times, so we link each execution to a thread.
t1 = threading.Thread(target=do_something) # Binds the function to a thread (function is not executed yet).
t2 = threading.Thread(target=do_something) # Binds the function to a thread (function is not executed yet).
t3 = threading.Thread(target=do_something) # Binds the function to a thread (function is not executed yet).

t1.start() # Starts the first thread.
t2.start() # Starts the second thread.
t3.start() # Starts the third thread.

t1.join() # Waits for the function to be completed before continuing to the last print of the program.
t2.join()
t3.join()

# Sets a finishing point to later calculate total execution time.
finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s).') # Prints out total execution time by taking the rounded result of start and end time.
