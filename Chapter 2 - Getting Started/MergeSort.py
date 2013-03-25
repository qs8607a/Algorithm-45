# Introduction to Algorithm - Chapter 2: Getting Started
# MERGE_SORT

def merge(left, right):
    res = [];
    i = 0;
    j = 0;
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]);
            i = i + 1;
        else:
            res.append(right[j]);
            j = j + 1;
    res += left[i:];
    res += right[j:];
    return res;

def mergeSort(arr):
    """
    sort array using a merge sort algorithm
    """
    if len(arr) <= 1:
        return;

    middle = int(len(arr)/2);
    left = mergeSort(arr[:middle]);
    right = mergeSort(arr[middle:]);
    merge(left, right);

