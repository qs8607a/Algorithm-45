# Introduction to Algorithm - Chapter 7 Quicksort
# QUICKSORT

def quickSort(arr):
    if not arr:
        return [];
    else:
        pivot = arr[0];
        less = [x for x in arr if x <  pivot]
        more = [x for x in arr[1:] if x >= pivot]
        return quickSort(less) + [pivot] + quickSort(more);
