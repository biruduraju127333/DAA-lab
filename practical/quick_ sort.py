# Quick Sort in Python

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    # Choose the pivot element
    pivot = arr[len(arr) // 2]

    # Divide the array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right parts
    return quick_sort(left) + middle + quick_sort(right)


# Main Program
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original List:", numbers)

sorted_numbers = quick_sort(numbers)

print("Sorted List:", sorted_numbers)
