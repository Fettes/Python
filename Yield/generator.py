# python中的generator：一边循环，一边计算
print([x * x for x in range(10)])
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
print(g)
# print the next item of the generator
# print(next(g))

# The method above is stupid, then we use for!!!
for n in g:
    print(n)

print("------------------Exercise2--------------------")
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()
print(next(g))
print("*" * 20)
print(next(g))
"""
-   g = foo() is supposed to be executed, but there is a yield in program which means it will not be executed 
    but create a generator
-   until next(), the program in foo() will be executed
-   when the program comes to yield, the program shut down. And RETURN 4!
-   if there is no another next(), the program will shut down forever.
-   However, there is a next(), the program will restart from the point where last time stop.
-   Then the program will print res, but, the previous return has returned the value, the res here is none!
-   Go ahead and print a 4
"""
print("------------------Exercise3-----------------------")
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()
print(next(g))
print("*" * 20)
print(g.send(7))
"""
-   Send() contains a next() function, as we said, the return here is none. However, if we use send(),
    the res can be assigned as 7.
-   Then next() in Send() will be executed to print another 4
"""
