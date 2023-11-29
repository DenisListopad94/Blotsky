def decorator_function(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] время выполнения {}, Функция протестирована: {}'.format(end - start, func.__name__))

    return wrapper


@decorator_function
def appear_numbers():
    n = list(range(0, 100))
    for item in n:
        print(item, end=" ")
    print(n)


appear_numbers()
