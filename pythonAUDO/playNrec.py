import threading

def task1():
    # Code for task 1
    print("Executing task 1")

def task2():
    # Code for task 2
    print("Executing task 2")

# Create thread objects
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Main program continues after the threads have finished
print("All threads have finished")
