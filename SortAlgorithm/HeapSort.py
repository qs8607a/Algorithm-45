# Introduction to Algorithm - Chapter 6: HeapSort  
# HEAP_SORT

def leftLeafIndex(i):
    return 2*i+1;

def rightLeafIndex(i):
    return 2*i+2;

def maxHeapify(arr, heapSize, i):
    l = leftLeafIndex(i);
    r = rightLeafIndex(i);

    largest = i;
    if l < heapSize and arr[l] > arr[i]:
        largest = l;
    if r < heapSize and arr[r] > arr[largest]:
        largest = r;
    if largest != i:
        tmp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = tmp;
        maxHeapify(arr, heapSize, largest);

def buildMaxHeap(arr):
    for i in range((int)((len(arr)-1)/2), -1, -1):
        maxHeapify(arr, len(arr), i);

def heapSort(arr):
    buildMaxHeap(arr);
    for i in range(len(arr)-1, 0, -1):
        # swap 
        tmp = arr[0];
        arr[0] = arr[i];
        arr[i] = tmp;
        maxHeapify(arr, i, 0);

