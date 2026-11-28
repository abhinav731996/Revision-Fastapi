# import asyncio

# async def task_one():
#     print("task one started")
#     await asyncio.sleep(2)
#     print('task one completed')

# async def task_two():
#     print("task two started")
#     await asyncio.sleep(2)
#     print("task two completed")

# async def main():
#     await asyncio.gather(
#         task_one(),
#         task_two()
#     )

# asyncio.run(main())



import asyncio

async def fetch_employee(employee_id):
    print(f"Fetching employee {employee_id}")
    await asyncio.sleep(2)

    return{
        "id" : employee_id,
        "name" : f"Employee {employee_id}"
    }

async def main():

    result = await asyncio.gather(
        fetch_employee(101),
        fetch_employee(102),
        fetch_employee(103)
    )

    for employee in result:
        print(employee)


asyncio.run(main())

