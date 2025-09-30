import math

def f(x):
    x1, x2 = x
    return x1 ** 4 + x2 ** 4 + (2 + x1 ** 2 + x2 ** 2) ** 0.5 - 2 * x1 + 3 * x2

def grad(x):
    x1, x2 = x
    return (4 * x1 ** 3 + x1 /(2 + x1 ** 2 + x2 ** 2) ** 0.5 - 2 ), (4 * x2 ** 3 + x2 /(2 + x1 ** 2 + x2 ** 2) ** 0.5 + 3 )

def difference(x,y, lambd = 1.0):
    z = [0] * len(x)
    for i in range(len(x)):
        z[i] = x[i] -  lambd * y[i]
    return z

def gradient_descent_const(x_start, epsilon = 10 ** (-6)):
    lambd = 0.5
    n = 1

    xk = x_start
    xk1 = difference(xk, grad(xk), lambd = lambd)
    while abs(f(xk1) - f(xk)) > epsilon:
        xk = xk1
        xk1 = difference(xk, grad(xk), lambd = lambd)
        n += 1
        while f(xk1) > f(xk):
            lambd /= 2
            xk1 = difference(xk, grad(xk), lambd=lambd)
            n+=1
    return xk1, f(xk1), n

if __name__ == '__main__':
    x_min, f_min, n = gradient_descent_const([0,0])
    print("Вектор х: " , x_min)
    print("Минимальное значение: ", f_min)
    print("Количество операций", n)
