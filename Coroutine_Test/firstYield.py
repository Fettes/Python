import asyncio
import random


async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        await asyncio.sleep(3)


async def mygen2(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        await asyncio.sleep(4)


strlist = ["ss", "dd", "gg"]
intlist = [1, 2, 5, 6]
c1 = mygen(strlist)
c2 = mygen2(intlist)
print(c1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [c1, c2]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()
