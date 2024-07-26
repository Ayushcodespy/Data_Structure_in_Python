array = [23,19,45,38,54,32,16]

n = len(array)
print(f"Unsorted array is : {array}\n")
for i in range (1, n):
    current = array[i]

    j= i-1

    while(j >= 0 and current < array[j]):
        array[j+1] = array[j]
        j -= 1

    array[j+1] = current

print(f"Sorted array is : {array}")