# Introduction to Algorithm - Chapter 2: Getting Started
# BUBBLESORT(A)

def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                tmp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = tmp;

