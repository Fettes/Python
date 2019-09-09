def fab(max_num):
    n1, a, b = 0, 0, 1
    while n1 < max_num:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n1 = n1 + 1


for n in fab(5):
    print(n)
