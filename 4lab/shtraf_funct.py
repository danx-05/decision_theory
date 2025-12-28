
def f(x):
    x1, x2 = x
    return shtraf_f(x)
    # return x1 ** 4 + x2 ** 4 + (2 + x1 ** 2 + x2 ** 2) ** 0.5 - 2 * x1 + 3 * x2

def shtraf_f(x):
    x1, x2 = x
    shtraf = 10**4 * (x1 + 3 * x2 - 4) ** 2
    # shtraf = 10 ** 4 * (2 * x1 - 3 * x2 ) ** 2

    return x1 ** 4 + x2 ** 4 + (2 + x1 ** 2 + x2 ** 2) ** 0.5 - 2 * x1 + 3 * x2 + shtraf


def method_XDg(x0, lambd = 1, epsilon = 10 ** (-6), alpha = 1):
    prev_min_f = f(x0)
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

        x7 = [x, y + lambd]
        x8 = [x, y - lambd]

        minn = 10 ** 7
        x_m = [0, 0]
        for i in [x1, x2, x3, x4, x5, x6, x7, x8]:
            if f(i) < minn:
                minn = f(i)
                x_m = i
        if minn >= prev_min_f:
            lambd /=2
            continue
        else:
            x_new = [x + alpha * (x_m[0] - x), y + alpha * (x_m[1] - y) ]
            if f(x_new) < prev_min_f:
                x0 = x_new
                prev_min_f = f(x_new)
            else:
                lambd /= 2

    return x0, f(x0), k


if __name__ == '__main__':
    x_min, f_min, n = method_XDg([0,0])
    print("Вектор х: ", x_min)
    print("Минимальное значение: ", f_min)
    print("Количество итерация", n)
