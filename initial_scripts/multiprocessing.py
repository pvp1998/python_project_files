import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeps for {seconds}")
    time.sleep(seconds)
    return "finished sleeping"

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# thread_list = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     thread_list.append(t)
#
# for thread in thread_list:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 1)} seconds')
