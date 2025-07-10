import sys

def trace_calls(func):
    func.depth = 0
    
    def wrapper(*args, **kwargs):
        indent = "  " * func.depth
        trace_msg = f"{indent}→ {func.__name__}({args[0]})"
        print(trace_msg)
        sys.stdout.flush()  # Force immediate output
        
        func.depth += 1
        result = func(*args, **kwargs)
        func.depth -= 1
        
        return_msg = f"{indent}← {func.__name__} returns {result}"
        print(return_msg)
        sys.stdout.flush()
        
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

if __name__ == "__main__":
    test_array = [64, 34, 25, 12]
    print("=" * 50)
    print("QUICKSORT TRACE")
    print("=" * 50)
    result = quicksort(test_array)
    print("=" * 50)
    print(f"FINAL RESULT: {result}")
