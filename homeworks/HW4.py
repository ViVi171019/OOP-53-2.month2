
def  check_type(func):
    def wrapper(num):
        if type (num) == int or type (num) == float:
            result = func(num)
        else:
            result = 'Ошибка: ожидалось число'
        return result
    return wrapper

@check_type
def square(x):
         return x * x

print(square('dd'))

def count_calls(func):
    def wrapper():
        if func:
            wrapper.count +=1
        result = wrapper.count
        print(f'Функция вызвана {result} раз')
        return func()

    wrapper.count = 0
    return wrapper


@count_calls
def hello():
    print("Привет!")


hello()
hello()
hello()
