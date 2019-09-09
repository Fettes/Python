class Fab(object):
    def __init__(self, max, ):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    # Add the function __iter__ in the class means that the object is iterable
    def __iter__(self):
        return self

    # Add the function in the class for providing an algorithm for the iterable object
    def __next__(self):
        if self.n < self.max:
            out = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return out
        raise StopIteration()


# 所以在定义一个可迭代类时，一般__iter__ 函数要与 __next__函数成对出现。__iter__函数向系统声明这个类可迭代，__next__定义了具体的迭代器。

for i in Fab(6):
    print(i)
