lst = [64, 34, 25, 5, 22, 11, 90, 12]
print(f"unsorted list : {lst}")

n = len(lst)

for i in range(n-1):
    min = i

    for j in range(i+1, n):
        if(lst[j] < lst[min]):
            min = j

    # swap the numbers if number is less than min_index number
    temp = lst[i]
    lst[i] = lst[min]
    lst[min] = temp

print(f"sorted list : {lst}")