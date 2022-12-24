import socket
import asyncio

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
    ser.bind(('', 51000))
    ser.listen(10)
    print("Server is running")
    conn, addr = ser.accept()
    while True:
        data = conn.recv(1024).decode()
        num_list = []
        for i in data:
            i = int(i)
            num_list.append(i)

        async def plus(nums):
            pl_num = nums[0] + nums[1]
            return pl_num
        async def minus(nums):
            mn_num = nums[0] + nums[1]
            return pl_mn
        async def multi(nums):
            mul_num = nums[0] + nums[1]
            return pl_mul

        loop = asyncio.get_event_loop()
        tasks = [loop.create_task(plus(num_list)),loop.create_task(minus(num_list)), loop.create_task(multi(num_list))]
        loop.run_until_complete(wait_tasks)

        results = f"Addition is: {tasks[0].result()};\n" \
                  f'Subtraction values is {tasks[1].result()};\n' \
                  f'Multiplication values is {tasks[2].result()}.'

        conn.send(message.encode())