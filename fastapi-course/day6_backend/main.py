import asyncio

async def task_one():
    print("task one started")
    await asyncio.sleep(2)
    print('task one completed')

async def task_two():
    print("task two started")
    await asyncio.sleep(2)
    print("task two completed")

async def main():
    await asyncio.gather(
        task_one(),
        task_two()
    )

asyncio.run(main())