from heapq import *


def merge_sorter(*args):
    heap = []
    iterators = []

    for index, item in enumerate(args):
        try:
            iterators.append(iter(item))
            heap.append((next(iterators[index]), index))
        except StopIteration:
            pass
    heapify(heap)

    while True:
        try:
            head_value, head_index = heappop(heap)
            yield head_value
            heappush(heap, (next(iter(iterators[head_index])), head_index))
        except IndexError:
            return
        except StopIteration:
            pass


a = sorted([4, 3, 1, 10])
b = sorted([3, 6, 7, 4, 9])
c = sorted([4, 3, 7, 8, 9, 19])
print(*merge_sorter(a, b, c))
