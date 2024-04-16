
array = [10,11,34,76,23,12,54,33]
print (f"Unorted array : {array}\n")

element = len(array)

def swap(a,b):
    temp = a
    a = b
    b = temp

for i in range(element):
    for j in range(element-1):
        if (array[j] > array[j+1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

print (f"Sorted array : {array}")