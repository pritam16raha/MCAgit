def insertionSort(arr):
     
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
 
#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [11,66,44,55,22,33,88,99,77]
arr2 = [11,22,33,44,55]
insertionSort(arr)
insertionSort(arr2)
print(arr)
print(arr2)