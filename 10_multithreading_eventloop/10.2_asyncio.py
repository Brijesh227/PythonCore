# Real example:
#   You cannot simply drop async and await into standard, blocking Python code. 
#   If a function contains blocking operations (like time.sleep() or requests.get()), it will freeze the entire event loop.

#   blocking            async code
#   time.sleep()  =>  await asyncio.sleep()
#   requests.get()  =>  httpx
#   sqlite3         => aiosqlite  

# Synchronus way: (blocking code)

import time
import requests

def fetch_sync(url):
    # This blocks the entire thread until the server responds
    response = requests.get(url)
    return response.status_code

def main_sync():
    urls = ["https://httpbin.org"] * 3
    start = time.time()
    
    # Sequential execution: takes ~6 seconds total
    results = [fetch_sync(url) for url in urls]
    
    print(time.time() - start)

# Asynchronous way (Concurrent execution):

import asyncio
import time
import httpx  # Async HTTP client

# 1. Mark the function as async
async def fetch_async(client, url):
    # 2. Use await on the network call
    response = await client.get(url)
    return response.status_code

async def main_async():
    urls = ["https://httpbin.org"] * 3
    start = time.time()
    
    # 3. Use an async context manager for the client
    async with httpx.AsyncClient() as client:
        # 4. Create a list of coroutine tasks
        tasks = [fetch_async(client, url) for url in urls]
        
        # 5. Run them concurrently; takes ~2 seconds total
        results = await asyncio.gather(*tasks)          # Actually happens: results = await asyncio.gather(coro1, coro2, coro3)

        
    print(time.time() - start)

# 6. Start the event loop
asyncio.run(main_async())


# Handling Unchangeable Blocking Code(like legacy library that doesn't support async)

import asyncio
import time

def legacy_blocking_function():
    time.sleep(2)  # Normal blocking sleep(let's assume legacy code here)
    return "Success"

async def main():
    # Runs the blocking function in a separate thread behind the scenes
    result = await asyncio.to_thread(legacy_blocking_function)
    print(result)

asyncio.run(main())

# Error handling in Asyncio task:
# biggest problem: 
#   If one task fails, gather immediately raises that exception to the main thread. 
#   The other tasks keep running in the background, but you lose immediate access to other task results.
#   - Wasted Resources, Ghost Actions

async def bad_task():
    raise ValueError("Something went wrong!")

async def good_task():
    await asyncio.sleep(1)
    return "Good data"

async def main():
    try:
        # Defaults to return_exceptions=False
        await asyncio.gather(bad_task(), good_task())
    except ValueError as e:
        print(f"Caught exception: {e}")

asyncio.run(main())

# TaskGroups: (structured concurrency) (python >3.11)
#   If one task fails, it actively and immediately cancels all other running tasks in the group so they don't waste resources or run as "ghosts".

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            # Schedule tasks into the background group
            task1 = tg.create_task(good_task())
            task2 = tg.create_task(bad_task())
            
        # If both succeeded, you would access them here:
        print(task1.result())
    except ExceptionGroup as eg:
        # Handles errors if any task within the group failed
        print(f"Handled group errors: {eg}")

asyncio.run(main())

