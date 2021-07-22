def fibonacci(x):
    a = 1
    b = 2
    for i in range(x):
        yield a
        (a, b) = (b, a+b)
for i in fibonacci(10):
    print(i)