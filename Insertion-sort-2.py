def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Take input from the user
arr = input("Enter the elements of the array separated by space: ").split()
# Convert input elements to integers
arr = [int(x) for x in arr]

# Call the insertion_sort function
insertion_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
