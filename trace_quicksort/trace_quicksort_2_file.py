def trace_calls(func):
    def wrapper(*args, **kwargs):
        trace_msg = f"🔍 Calling {func.__name__} with args: {args}\n"
        print(trace_msg, end='')
        
        # Also write to file
        with open('trace_output.txt', 'a') as f:
            f.write(trace_msg)
        
        result = func(*args, **kwargs)
        
        return_msg = f"📤 {func.__name__} returning: {result}\n"
        print(return_msg, end='')
        
        with open('trace_output.txt', 'a') as f:
            f.write(return_msg)
        
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

# Clear the trace file and run
if __name__ == "__main__":
    # Clear previous traces
    open('trace_output.txt', 'w').close()
    
    test_array = [64, 34, 25, 12]
    print("Running quicksort with file tracing...")
    result = quicksort(test_array)
    print(f"Final result: {result}")
    print("Check 'trace_output.txt' for detailed trace!")
