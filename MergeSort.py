
def merge_sort(arr):
    
    l = int(len(arr))
    if l == 1:
        return arr
    
    arr1 = merge_sort(arr[:int(l/2)])
    arr2 = merge_sort(arr[int(l/2):])

    arr = merge(arr1,arr2)

    return arr

def merge(arr1,arr2):
    arr = []

    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] > arr2[0]:
            arr.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            arr.append(arr1[0])
            arr1.remove(arr1[0])
        
    while len(arr1) != 0:
        arr.append(arr1[0])
        arr1.remove(arr1[0])

    while len(arr2) != 0:
        arr.append(arr2[0])
        arr2.remove(arr2[0])

    return arr

arr = merge_sort([7,3,1,5,2,9,4,6])
print(arr)
