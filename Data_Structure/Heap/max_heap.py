def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i/2

def max_heapify(heap, heap_size, i): # i = node index (where need to hipipy)
    l = left(i)
    r = right(i)
    largest = i

    if (l< heap_size) and (heap[l] > heap[i]):
        largest = l

    else:
        largest = i

    if r < heap_size and heap[r] > heap[largest]:
        largest = r

    if (largest != i):
        t = heap[i]
        heap[i] = heap[largest]
        heap[largest] = t

        max_heapify(heap, heap_size, largest)

heap = [10, 15, 30, 40, 50, 100, 40]
ln = len(heap)

print(heap)
print('-----------------------')
print('After hipipy')

max_heapify(heap, ln, 0)
print(heap)