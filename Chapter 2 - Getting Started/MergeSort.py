# Introduction to Algorithm - Chapter 2: Getting Started
# MERGE_SORT

import sys
import math

def merge(arr, p, q, r):
    """
    merge two arry into one with a perticular order
    """
    if p < 0 or  p > q or q >= r:
        print "parameter not valid";
        return;

    leftArr = arr[p:q+1];
    leftArr.append(sys.maxint);
    if r == len(arr) - 1:
        rightArr = arr[q+1:];
    else:
        rightArr = arr[q+1:r+1];
    rightArr.append(sys.maxint);

    i = 0;
    j = 0;
    for k in range(p, r+1):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i];
            i += 1;
        else:
            arr[k] = rightArr[j];
            j += 1;

def mergeSort(arr, p, r):
    """
    sort array using a merge sort algorithm
    """
    if p < r:
        q = int(math.floor((p+r)/2));
        mergeSort(arr, p, q);
        mergeSort(arr, q+1, r);
        merge(arr, p, q, r);

