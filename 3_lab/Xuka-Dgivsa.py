import math


def f(x):
    x1, x2 = x
    return x1 ** 4 + x2 ** 4 + (2 + x1 ** 2 + x2 ** 2) ** 0.5 - 2 * x1 + 3 * x2


def method_XDg(x0, lambd, alpha, epsilon = 10**(-6)):
    k = 0
    while lambd > epsilon:
        k += 1
        x, y = x0
        x1 = [x + lambd, y + lambd]
        x2 = [x + lambd, y]
        x3 = [x + lambd, y - lambd]

        x4 = [x - lambd, y + lambd]
        x5 = [x - lambd, y]
        x6 = [x - lambd, y - lambd]

        x7 = [x , y + lambd]
        x8 = [x , y - lambd]
        minn = 10**7
        x_m = [0,0]
        for i in [x1,x2,x3,x4,x5,x6,x7,x8]:
            if f(i) < minn:
                minn = f(i)
                x_m = i
        if f(x0) < minn:
            lambd /= 2
        else:
            x1 = [x + alpha * (x_m[0] - x), y + alpha * (x_m[1] - y) ]
            if f(x1) > f(x0):
                alpha /= 2
            x0 = x1
        print(x0, lambd)
    return x0, k


if __name__ == '__main__':
    print(method_XDg([0,0], 1, 2))




