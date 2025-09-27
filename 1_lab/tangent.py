import math
h = 10 ** (-7)
def f(x):
    return 2 + x ** 2 + x ** (2/3) - math.log(1 + x ** (2/3)) - 2 * x * math.atan(x) ** (1/3)
def diff(x):
    return (f(x+h) - f(x)) / h
def direct (x, k, b):
    return k * x + b
def union(a,b):
    return ( f(a) - f(b) - diff(a) * a + diff(b) * b ) / (diff(b) - diff(a))

def tangent(a,b,epsilon = 10 ** (-6)):
    x_m = union(a,b)
    k = diff(b)
    c = f(b) - diff(b) * b

    n = 0
    while abs(f(x_m) - direct(x_m, k, c)) > epsilon:
        n += 1
        if diff(x_m) < 0:
            a = x_m
            x_m = union(a, b)
        else:
            b = x_m
            x_m = union(x_m, a)
            k = diff(b)
            c = f(b) - diff(b) * b
    return (a+b)/2, n
if __name__ == '__main__':
    x_min, n = tangent(0.5, 1)
    print("Точка минимума: ", x_min)
    print("Наименьшее значение: ", f(x_min))
    print("Количество итераций: ", n)
