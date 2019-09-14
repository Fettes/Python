# asyncio_cancel_task2.py
import asyncio


async def task_func(loop):
    print('in task_func, sleeping')
    try:
        # task = loop.create_task(hello_fuc())
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print('task_func was canceled')
        raise
    return 'the result'


async def hello_fuc():
    print('Hello world')


def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('canceled the task')


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func(loop))
    task2 = loop.create_task(hello_fuc())
    await task2
    loop.call_later(1, task_canceller, task)
    # loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('main() also sees task as canceled')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
