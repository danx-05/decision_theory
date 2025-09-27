import math

def f(x):
    return 2 + x ** 2 + x ** (2/3) - math.log(1 + x ** (2/3)) - 2 * x * math.atan(x) ** (1/3)

def golden(a, b, epsilon = 10 ** (-6)):
    n = 0
    x1 = a + (3 - 5 ** (1 / 2)) * (b - a) / 2
    x2 = a + (5 ** (1 / 2) - 1) / 2 * (b - a)
    fx1 = f(x1)
    fx2 = f(x2)
    while abs(b - a) > epsilon:
        n += 1
        if fx1 > fx2:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + (5 ** (1 / 2) - 1) / 2 * (b - a)
            fx2 = f(x2)
        else:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = a + (3 - 5 ** (1 / 2)) * (b - a) / 2
            fx1 = f(x1)
    return (a+b)/2, n

if __name__ == '__main__':
    x_min, n = golden(0.5, 1)
    print("Точка минимума: ", x_min)
    print("Наименьшее значение: ", f(x_min))
    print("Количество итераций: ", n)

