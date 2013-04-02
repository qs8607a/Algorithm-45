# Introduction to Algorithm - Chapter 8: Sorting in Linear Time
# COUNTING-SORT

def countingSort(arr, maxValue):
    res = [0] * len(arr);
    countArr = [0] * (maxValue+1); 

    for i in range(0, len(arr)):
        countArr[arr[i]] = countArr[arr[i]] + 1;
    for i in range(1, maxValue+1):
        countArr[i] = countArr[i] + countArr[i-1];
        
    print countArr;
    for i in range(len(arr)-1, -1, -1):
        res[countArr[arr[i]]-1] = arr[i];
        countArr[arr[i]] = countArr[arr[i]] - 1;

    return res;

