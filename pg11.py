import queue
import threading
import time

def basic_task(name):
    for i in range(3):
        print(f"{name} : {i + 1}")
        time.sleep(1)

def basic_threading_demo():
    t1 = threading.Thread(target=basic_task, args=("Thread1", ))
    t2 = threading.Thread(target=basic_task, args=("Thread2", ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Basic Threading demo completed")

# threading with arguements

def print_numbers(name, limit):
    for i in range(1, limit+1):
        print(f"{name} : {i}")
        time.sleep(1)

def threading_with_args():
    t1 = threading.Thread(target=print_numbers, args=("Thread1", 5))
    t2 = threading.Thread(target=print_numbers, args=("Thread2", 5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threading with arguments demo completed")


# producer & consumer problem

q = queue.Queue()

def producer():
    for i in range(5):
        item = f"Item -{i}"
        q.put(item)
        print(f"Produced {item}")
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")
        time.sleep(1)

def producer_consumer_demo():
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Producer-Consumer demo completed")

def menu():
    print("\n1. Basic Threading demo")
    print("2. Threading with arguments demo")
    print("3. Producer-Consumer demo")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            basic_threading_demo()
        elif choice == 2:
            threading_with_args()
        elif choice == 3:
            producer_consumer_demo()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()