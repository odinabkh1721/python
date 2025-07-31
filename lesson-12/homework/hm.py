
# Task 1


import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result_list):
    for number in range(start, end):
        if is_prime(number):
            result_list.append(number)

def main():
    start_range = 1
    end_range = 100
    thread_count = 4

    threads = []
    primes = []

    lock = threading.Lock()

    step = (end_range - start_range) // thread_count

    for i in range(thread_count):
        sub_start = start_range + i * step
        sub_end = start_range + (i + 1) * step if i != thread_count - 1 else end_range

        thread_result = []

        def thread_task(s=sub_start, e=sub_end, lst=thread_result):
            check_primes_in_range(s, e, lst)
            with lock:
                primes.extend(lst)

        t = threading.Thread(target=thread_task)
        threads.append(t)
        t.start()

   
    for t in threads:
        t.join()

    print("Topilgan tub sonlar:", sorted(primes))

if __name__ == "__main__":
    main()



# Task 2 
import threading
from collections import Counter
import os


def count_words(lines, local_counter):
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)

def threaded_word_count(filename, thread_count=4):
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    step = total_lines // thread_count

    threads = []
    counters = []

    for i in range(thread_count):
        start = i * step
        end = (i + 1) * step if i != thread_count - 1 else total_lines
        chunk = lines[start:end]
        local_counter = Counter()
        counters.append(local_counter)

        t = threading.Thread(target=count_words, args=(chunk, local_counter))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

  
    final_counter = Counter()
    for c in counters:
        final_counter.update(c)

   
    for word, count in final_counter.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = "large_text.txt"  
    if os.path.exists(filename):
        threaded_word_count(filename)
    else:
        print("Fayl topilmadi. Iltimos, 'large_text.txt' faylini mavjud qiling.")
