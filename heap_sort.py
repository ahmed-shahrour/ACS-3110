from binaryheap import BinaryMinHeap

def heap_sort(items):
    heap = BinaryMinHeap(items)
    heap.build_min_heap()
    heap.heapify(0, heap.size())

    last_element = heap.size() - 1;
    while last_element > 0:
        heap.swap(0, last_element)
        heap.heapify(0, last_element)
        last_element -= 1