import threading
from concurrent.futures import ThreadPoolExecutor


a = 0
lock = threading.Lock()


def function(arg):
    global a
    for _ in range(arg):
        with lock:
            a += 1


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(function, 1000000)

    print("----------------------", a)  # ???


main()
