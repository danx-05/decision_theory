import math

def f(x):
    return 2 + x ** 2 + x ** (2/3) - math.log(1 + x ** (2/3)) - 2 * x * math.atan(x) ** (1/3)
    # return x ** 2

def diff(x, h = 10 ** (-7)):
    return (f(x+h) - f(x)) / h
def diff_2(x, h = 10 ** (-7)):
    return (diff(x+h) - diff(x)) / h

def Njuton(a, b, epsilon = 10 ** (-6)):
    n = 1
    x_0 = b
    x_1 = x_0 - diff(x_0) / diff_2(x_0)
    while abs(x_0 - x_1) > epsilon:
        x_0 = x_1
        x_1 = x_0 - diff(x_0) / diff_2(x_0)
        n += 1
    return x_1, n

if __name__ == '__main__':
    x_min, n = Njuton(0.5, 1)
    print("Точка минимума: ", x_min)
    print("Наименьшее значение: ", f(x_min))
    print("Количество итераций: ", n)