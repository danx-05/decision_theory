import math

def f(x):
    return -x ** 3 + 3 * (1 + x) * (math.log(x + 1) - 1)


def df(x):
    """Первая производная функции f(x)"""
    return -3 * x ** 2 + 3 * (math.log(x + 1) - 1) + 3 * (1 + x) / (x + 1)


def d2f(x):
    """Вторая производная функции f(x)"""
    return -6 * x + 3 / (x + 1) - 3 * (1 + x) / ((x + 1) ** 2)


# def f(x):
#     return 2 + x ** 2 + x ** (2/3) - math.log(1 + x ** (2/3)) - 2 * x * math.atan(x) ** (1/3)
#     # return x ** 2

def diff(x, h = 10 ** (-7)):
    return (f(x+h) - f(x)) / h
def diff_2(x, h = 10 ** (-7)):
    return (diff(x+h) - diff(x)) / h

def Njuton(a, b, epsilon = 10 ** (-6)):
    n = 1
    x_0 = b
    x_1 = x_0 - df(x_0) / d2f(x_0)
    while abs(x_0 - x_1) > epsilon:
        x_0 = x_1
        x_1 = x_0 - df(x_0) / d2f(x_0)
        n += 1
    return x_1, n

if __name__ == '__main__':
    x_min, n = Njuton(a = -0.5, b = 0.5)
    print("Точка минимума: ", x_min)
    print("Наименьшее значение: ", f(x_min))
    print("Количество итераций: ", n)