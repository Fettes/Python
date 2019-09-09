# python中的generator：一边循环，一边计算
print([x*x for x in range(10)])
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x*x for x in range(10))
print(g)
# print the next item of the generator
# print(next(g))

# The method above is stupid, then we use for!!!
for n in g:
    print(n)


