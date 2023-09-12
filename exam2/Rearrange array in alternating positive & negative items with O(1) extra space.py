def rearrange(arr):
    n = len(arr)
    temp = -1
    
    for index in range(n):
        if temp >= 0:
            if (arr[index] >= 0 and arr[temp] < 0) or (arr[index] < 0 and arr[temp] >= 0):
                tempRotate = arr[index]
                for i in range(index, temp, -1):
                    arr[i] = arr[i - 1]
                arr[temp] = tempRotate
                if index - temp > 2:
                    temp += 2
                else:
                    temp = -1

        if temp == -1:
            if (arr[index] >= 0 and index % 2 == 0) or (arr[index] < 0 and index % 2 == 1):
                temp = index

    return arr


# Driver Code
arr = [-5, -2, 5, 2, 4,
	7, 1, 8, 0, -8]

print("Given Array is:")
print(arr)

print("\nRearranged array is:")
print(rearrange(arr))
