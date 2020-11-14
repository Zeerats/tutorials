### Threading example using the 'threading' module and creating 10 threads using a loop.
# The function that is passed to the thread accepts a function.

import threading
import time


# Sets a starting point to later calculate total execution time.
start = time.perf_counter()

# Now the function takes an argument for the seconds. This will be handled and passed when the threads are created, using the 'args' argument.
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping.')


threads = [] # Creates a list of threads to append the created threads in the for loop.

# This loop will create, start and append the threads to the list.
for _ in range(10): # Underscore is a throw-away variable, since it won't be used for anything.
    t = threading.Thread(target=do_something, args=[1.5]) # The 'args' argument will be passed to the function, as it can't be passed manually (it would execute the function here).
    t.start()
    threads.append(t)

# Joining (so they wait for the completion of the function) the threads created before.
for thread in threads:
    thread.join()

# Sets a finishing point to later calculate total execution time.
finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s).') # Prints out total execution time by taking the rounded result of start and end time.
