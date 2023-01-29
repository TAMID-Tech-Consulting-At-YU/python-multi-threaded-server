import multiprocessing
from collections import Counter
import os

import Timer

result_list = Counter()


def worker(offset, length, filename):
    file = open(filename, 'r')
    file.seek(offset)
    content = file.read(length).lower()
    words = content.split()
    result = Counter(words)
    file.close()
    return result


def update_counter(result):
    result_list.update(result)


def sequential():
    filename = "document.txt"
    file_size = os.stat(filename)[6]
    work_result = worker(0, file_size, filename)
    update_counter(work_result)
    print(result_list.most_common(40))


def partition_into_chunks(filename, file_size, processes):
    chunks = []
    origin = open(filename, 'r')
    while True:
        lines = origin.readlines(file_size // processes)
        if not lines:
            break
        chunks.append("\n".join(lines))
    return chunks


def parallel():
    processes = 5
    pool = multiprocessing.Pool(processes=processes)
    filename = "document.txt"
    file_size = os.stat(filename)[6]
    chunks = partition_into_chunks(filename, file_size, processes)
    # Get the length of each chunk
    lengths = [len(chunk) for chunk in chunks]
    # start partitions at offset 0
    offset = 0
    # Give each partition to its own thread
    for length in lengths:
        pool.apply_async(worker, args=(offset, length, filename,), callback=update_counter)
        # Start at the next chunk
        offset += length

    pool.close()
    pool.join()
    print(result_list.most_common(40))


if __name__ == "__main__":
    result_list.clear()
    t = Timer.Timer()
    parallel()
    t.stop()

    result_list.clear()
    t = Timer.Timer()
    sequential()
    t.stop()
