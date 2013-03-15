# Introduction to Algorithm - Chapter 2 Getting Started 
# INSERT_SORT(A)

def insertSort(arr):
    """
    insertSort function sort all elements (numbers) in arr inscreasly.
    """
    assert isinstance(arr, list);

    if len(arr) <= 1:
        return arr;

    for j in range(1,len(arr)-1):
        key = arr[j];

        # Insert arr[j] into the sorted seqence arr[0, ..., j-1]
        i = j - 1;
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i];
            i = i - 1;
            arr[i+1] = key;

    return arr;

