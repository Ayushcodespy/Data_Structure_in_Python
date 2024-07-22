lst = [12,65,34,90,65,76,85,39,29,81]
length = len(lst)

def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        

print(lst)
bubblesort(lst)
print(lst)