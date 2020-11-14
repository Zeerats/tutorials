### Threading example using the 'threading' module and creating 10 threads using a loop.

import threading
import time


# Sets a starting point to later calculate total execution time.
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping.')


threads = [] # Creates a list of threads to append the created threads in the for loop.

# This loop will create, start and append the threads to the list.
for _ in range(10): # Underscore is a throw-away variable, since it won't be used for anything.
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

# Joining (so they wait for the completion of the function) the threads created before.
for thread in threads:
    thread.join()

# Sets a finishing point to later calculate total execution time.
finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s).') # Prints out total execution time by taking the rounded result of start and end time.
