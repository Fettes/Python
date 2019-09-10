import asyncio


async def fun():
    print('hello word')

loop = asyncio.get_event_loop()
loop.run_until_complete(fun())

