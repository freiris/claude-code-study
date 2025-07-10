import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('quicksort_trace.log'),
        logging.StreamHandler()  # This ensures console output
    ]
)

def trace_calls(func):
    def wrapper(*args, **kwargs):
        logging.info(f"🔍 Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        logging.info(f"📤 {func.__name__} returning: {result}")
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
    print("Starting quicksort with logging...")
    result = quicksort(test_array)
    print(f"Final result: {result}")
