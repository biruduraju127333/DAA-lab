# Merge Sort in Python

# Function to merge two sorted subarrays
def merge(arr, left, mid, right):

    # Find sizes of two subarrays
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr
    i = 0      # Initial index of first subarray
    j = 0      # Initial index of second subarray
    k = left   # Initial index of merged array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Merge Sort function
def merge_sort(arr, left, right):

    if left < right:

        # Find the middle point
        mid = (left + right) // 2

        # Sort first half
        merge_sort(arr, left, mid)

        # Sort second half
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)


# Main Program
arr = [38, 27, 43, 3, 9, 82, 10, 15, 22, 55]

print("Original Array:")
print(arr)

merge_sort(arr, 0, len(arr) - 1)

print("\nSorted Array:")
print(arr)
