from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()

if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is', shared_number.value)


def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        # lock the state
        lock.acquire()

        number.value += 1

        # unlock the state
        lock.release()

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            lock.acquire()
            numbers[i] += 1
            lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()

    shared_number = Value('i', 0)
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    # pass the lock to the target function
    process1 = Process(target=add_100, args=(shared_number, lock))
    process2 = Process(target=add_100, args=(shared_number, lock))

    process3 = Process(target=add_100_array, args=(shared_array, lock))
    process4 = Process(target=add_100_array, args=(shared_array, lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')



from multiprocessing import Queue

# create queue
q = Queue()

# add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1

# now q looks like this:
# back --> 3 2 1 --> front

# get and remove first element
first = q.get() # --> 1
print(first)

# q looks like this:
# back --> 3 2 --> front

# communicate between processes with the multiprocessing Queue
# Queues are thread and process safe
from multiprocessing import Process, Queue

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

if __name__ == "__main__":

    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())

    print('end main')
# back --> 3 2 1 --> front

# get and remove first element
first = q.get() # --> 1
print(first)

# q looks like this:
# back --> 3 2 --> front