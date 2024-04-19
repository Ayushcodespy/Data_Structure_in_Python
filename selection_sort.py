array = []
loop = int(input("Enter length of the array : "))
for x in range(loop):
    element = int(input(f"Enter element {x+1} : "))
    array.append(element)

print(f"Unsorted array : {array}")

for i in range(loop-1):
    min_index = i
    for j in range(i+1 , loop):
        # min_index = i
        if(array[j] < array[min_index]):
           min_index = j
    
    value = array.pop(min_index)
    array.insert(i, value)

print(f"Sorted array is : {array}")
    
