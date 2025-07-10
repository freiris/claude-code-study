def quicksort(arr):
    """
    Buggy quicksort implementation - contains a single common mistake
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # Choose first element as pivot
    left = []
    right = []
    
    # Partition the array
    for element in arr:  # BUG: This includes the pivot element!
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    
    # Recursively sort left and right partitions
    return quicksort(left) + [pivot] + quicksort(right)

# Test the buggy quicksort
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    
    sorted_array = quicksort(test_array)
    print("Sorted array:", sorted_array)
    
    # Test with edge cases
    print("\nEdge case tests:")
    print("Empty array:", quicksort([]))
    print("Single element:", quicksort([42]))
    print("Duplicates:", quicksort([5, 2, 8, 2, 9, 1, 5, 5]))
