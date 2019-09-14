# ensure_future.py
import asyncio


async def wrapped():
    print('6 wrapped')
    return 'result'


async def inner(task):
    print('11 inner: starting')
    print('12 inner: waiting for {!r}'.format(task))
    result = await task 
    print('14 inner: task returned {!r}'.format(result))


async def starter():
    print('18 starter: creating task')
    # 需要注意的是，传入 ensure_future() 的 coroutine 不会立马启动，
    # 需要有某个地方使用了 await 语句操作创建的 task 的时候它才会被执行。
    task = asyncio.ensure_future(wrapped())
    print('22 starter: waiting for inner')
    await inner(task)
    print('24 starter: inner returned')


event_loop = asyncio.get_event_loop()
try:
    print('29 entering event loop')
    result = event_loop.run_until_complete(starter())
finally:
    event_loop.close()
