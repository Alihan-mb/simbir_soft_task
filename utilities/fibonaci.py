from datetime import datetime


def fibonacci(n):
    if n <= 0:
        return "Число должно быть больше нуля"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[-1]


today = datetime.now().day
result = fibonacci(today + 1)
