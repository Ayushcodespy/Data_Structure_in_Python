array = []
loop = int(input("How many elements you want to enter in array : "))
for x in range(loop):
    value = int(input(f"Enter value {x+1} : "))
    array.append(value)


print (f"\nUnorted array : {array}\n")

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

print (f"Sorted array : {array}\n")