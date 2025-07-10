def trace_calls(func):
    def wrapper(*args, **kwargs):
        print(f"🔍 Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"📤 {func.__name__} returning: {result}")
        return result
    return wrapper

@trace_calls
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

# ADD THIS: Actually call the function!
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Testing quicksort with tracing:")
    result = quicksort(test_array)
    print(f"Final result: {result}")
