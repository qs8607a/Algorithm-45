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


def testInsertSort(arr):
    """
    testcase for insertSort.
    """
    insertSortRes = arr;
    insertSortRes = insertSort(insertSortRes);
    print(insertSortRes);
    sortRes = arr;
    sortRes.sort();
    print(sortRes);

if __name__ == "__main__":
    arr = [1,7,6,5,3,0,8,90];
    print(arr);
    testInsertSort(arr);

    arr = [1];
    print(arr);
    testInsertSort(arr);

    arr = [];
    print(arr);
    testInsertSort(arr);

