import math

def f(x):
    return 2 + x ** 2 + x ** (2/3) - math.log(1 + x ** (2/3)) - 2 * x * math.atan(x) ** (1/3)

a = 0.5
b = 1

delta = 10**(-7)
epsilon = 10 ** (-6)

n = 0

while abs(b - a) > epsilon:
    n += 1
    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2
    if f(x1) > f(x2):
        a = x1
    else:
        b = x2
print((a+b)/2)
print("Количество итераций:", n)