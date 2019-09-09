# Return next item in iterator:next(iterator[, default])
"""
"default" is the number that returned by the iterator when there is no more item in iterator
If there is no default number and the iterator reaches the bound. There will be a exception named: StopIteration
"""
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
# 如果传入第二个参数, 获取最后一个元素之后, 下一次next返回该默认值, 而不会抛出 StopIteration:
it = iter([1, 2, 5, 4, 3])
while True:
    x = next(it, 'a')
    print(x)
    if x == 'a':
        break
