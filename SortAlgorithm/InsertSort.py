# Introduction to Algorithm - Chapter 2 Getting Started 
# INSERT_SORT(A)

def insertSort(arr):
    """
    insertSort function sort all elements (numbers) in arr inscreasly.
    """
    for i in range(1, len(arr)):
        key = arr[i];

        # Insert arr[j] into the sorted seqence arr[0, ..., j-1]
        j = i - 1;
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j];
            arr[j] = key;
            j = j - 1;


