from claude_code_sdk import query, ClaudeCodeOptions
import asyncio
import logging
import yaml

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('claude_trace.log'),
        # This ensures console output
        logging.StreamHandler()  
        ]
)

def trace_calls(func):
    def wrapper(*args, **kwargs):
        logging.info(f"🔍 Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        logging.info(f"📤 {func.__name__} returning: {result}")
        return result
    return wrapper

# Batch process prompts with Claude Code
@trace_calls
async def process_batch_prompts(prompts):
    results = []
     
    for prompt_data in prompts:
        print(prompt_data)
        
        options = ClaudeCodeOptions(
            max_turns=3,
            allowed_tools=["Read", "Write", "Bash"],
        )
        
        messages = []
        async for message in query(
            prompt=prompt_data["prompt"],
            options=options
        ):
            messages.append(message)
        
        results.append({
            "id": prompt_data["id"],
            "messages": messages
        })
    
    return results

# Save results to yaml
def save_as_yaml(results):
    # Convert SystemMessage objects to dictionaries
    converted_results = []
    for result in results:
        if isinstance(result, dict) and 'messages' in result:
            converted_result = result.copy()
            converted_result['messages'] = [
                {'type': type(msg).__name__, 'content': str(msg)}
                for msg in result['messages']
            ]
            converted_results.append(converted_result)
    with open("claude_results.yaml", 'w') as f:
        yaml.dump(converted_results, f, indent=2)



if __name__ == "__main__":
    # we use Claude to generate three example codes, and ask Claude Code to process the prompts 
    prompts = [
        {"id": "task-1", "prompt": "Create a unit test for coin_change.py, save the result in coin_change_with_unit_test.py"},
        {"id": "task-2", "prompt": "Optimize this database query in customer_order.sql, save the result in customer_order_optimized.sql"},
        {"id": "task-3", "prompt": "Fix the bug in buggy_quick_sort.py, save the result in fixed_quick_sort.py"}
]
    print("Starting process_batch_prompts with logging...")

    results = asyncio.run(process_batch_prompts(prompts))
    save_as_yaml(results)
    print(f"Final results: {results}")
