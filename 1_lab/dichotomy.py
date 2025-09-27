import math

def f(x):
    return 2 + x ** 2 + x ** (2/3) - math.log(1 + x ** (2/3)) - 2 * x * (math.atan(x) ) ** (1/3)

def dichotomy(a, b, epsilon = 10 ** (-6), delta = 10 ** (-7)):
    # a = 0.5
    # b = 1
    n = 0
    while abs(b - a) > epsilon:
        n += 1
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
    return (a+b) / 2, n


if __name__ == '__main__':
    x_min, n = dichotomy(0.5, 1)
    print("Точка минимума: ", x_min)
    print("Наименьшее значение: ", f(x_min))
    print("Количество итераций: ", n)
