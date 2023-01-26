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

    # After running the driver you will see that the output will have "Finished in 0.0 second(s)"

    # This is because when we pass the work to the three threads we are offloading the work from the main thread
    # ,and it can continue executing the code to stop the timer

    # "joining" a thread means let the main thread wait for the thread doing the work to finish before stopping the
    # timer

    # TODO uncomment these joins to tell the main thread to wait for them to finish and re-run the code,
    #  observe the output

    # thread_one.join()
    # thread_two.join()
    # thread_three.join()


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
    run_timed_test(multiple_threads)


driver()
