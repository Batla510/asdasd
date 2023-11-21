import asyncio
import time

async def summ(a,b):
    await asyncio.sleep(1)
    print(a+b)
async def slow(a,b):
    await asyncio.sleep(5)
    print(a*b)
async def main():
    start = time.time()
    task1 = asyncio.create_task(summ(12,2))
    task2 = asyncio.create_task(slow(5,5))
    await task1
    await task2
    end = time.time()
    print(f'Времени прошло:{end - start:.2f} секунд')


asyncio.run(main())
