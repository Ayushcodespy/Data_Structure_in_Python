

def devide(arr):
    if(len(arr) <= 1):
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    l = devide(left)
    r = devide(right)
    return merge(l,r)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            sorted_arr.append(left[i])
            i = i+1

        else:
            sorted_arr.append(right[j])
            j = j+1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr



lst = [23,65,21,45,65,12,87,36,19]
print(f" Unsorted List is : {lst}")
print(f" Sorted List is : {devide(lst)}")