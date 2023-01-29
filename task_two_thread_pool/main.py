from concurrent.futures import ThreadPoolExecutor

from Timer import Timer
from time import sleep
import threading  # thread library

'''
        *************
        *   Tasks   *
        *************
'''


def one_second_of_work():
    print(f'{threading.current_thread().name} starting work...')
    sleep(1)
    print(f'{threading.current_thread().name} finished work')


# Completed method
def n_second_of_work(n):
    print(f'{threading.current_thread().name} starting work...')
    sleep(n)
    print(f'{threading.current_thread().name} finished work')


'''
        ***********************
        *   Runnable Methods  *
        ***********************
'''


# This method will use the [main] thread to run n amount of work
def sequential_thread():
    one_second_of_work()  # One second
    one_second_of_work()  # Two seconds
    one_second_of_work()  # Three seconds


def multiple_threads():
    # initialize three threads each of them should do a second of work
    thread_one = threading.Thread(target=one_second_of_work)
    thread_two = threading.Thread(target=one_second_of_work)
    thread_three = threading.Thread(target=one_second_of_work)

    # Start the threads work

    # You will see that each thread gets its own thread name and id
    # and each thread will start at the same time, they dont have to wait for each other
    thread_one.start()
    thread_two.start()
    thread_three.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()


# TODO Now that we can save references to thread objects lets add them to a list
#   this will allow us to create a 'pool' of threads
#   either running or task, waiting to give results back or ready for a new task

# Omit this code
def thread_pool():
    pool = []
    for _ in range(3):
        thread = threading.Thread(target=one_second_of_work)
        pool.append(thread)
        thread.start()

    for thread in pool:
        thread.join()


# TODO Use Python libraries to accomplish the same task as above
def thread_pool_executor():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for _ in range(3):
            future = executor.submit(one_second_of_work)
            futures.append(future)

        for future in futures:
            future.result()


'''
        *****************
        *   Timer Test  *
        *****************
'''


def run_timed_test(method_to_run):
    timer = Timer()
    method_to_run()
    timer.stop()


'''
        *****************
        *   Start Here  *
        *****************
'''


# This is the main driver to run both sequential and parallel work
def driver():
    # Here for formatting purposes
    divider_len = 10
    divider = "=" * divider_len

    # Start the timed sequential work
    print(f'{divider}Starting sequential work{divider}')
    run_timed_test(sequential_thread)

    # Start the timed parallel work
    print(f'{divider}Starting parallel work{divider} ')
    run_timed_test(thread_pool_executor)


driver()
