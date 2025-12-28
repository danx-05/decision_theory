
def f(x):
    x1, x2 = x
    return x1 ** 4 + x2 ** 4 + (2 + x1 ** 2 + x2 ** 2) ** 0.5 - 2 * x1 + 3 * x2




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

import math

def f(x):
    x1, x2 = x
    return x1 ** 4 + x2 ** 4 + math.sqrt(2 + x1 ** 2 + x2 ** 2) - 2 * x1 + 3 * x2
def error(triangle):
        f_triangle = [f(i) for i in triangle]

        mean = sum(f_triangle) / 3
        er = 0
        for i in range(3):
            er += (f_triangle[i] - mean) ** 2
        return math.sqrt(er/3)
def Nerdera_Mida(x0, alpha = 0.9, gamma = 2, beta = 0.53, epsilon = 10 ** (-6)):
    x1 = [x0[0], x0[1]]
    x2 = [x0[0]+1, x0[1]]
    x3 = [x0[0], x0[1]+1]
    triangle = [x1, x2, x3]
    k = 0
    while error(triangle) > epsilon:
        k += 1
        f_triangle = [f(i) for i in triangle]

        i_l = min(range(3), key=lambda i: f_triangle[i])
        i_h = max(range(3), key=lambda i: f_triangle[i])
        i_g = 3 - i_l - i_h

        x_l, x_g, x_h = triangle[i_l], triangle[i_g], triangle[i_h]
        f_l, f_g, f_h = f_triangle[i_l], f_triangle[i_g], f_triangle[i_h]
        triangle = [x_l, x_g, x_h ]
        f_triangle = [f_l, f_g, f_h]
        x_c = [(x_l[0] + x_g[0]) / 2,
               (x_l[1] + x_g[1]) / 2]
        # Отражение
        x_r = [
            (1 + alpha) * x_c[0] - alpha * x_h[0],
            (1 + alpha) * x_c[1] - alpha * x_h[1]
        ]
        f_r = f(x_r)
        if f_r < f_l:
            # Растяжение
            x_e = [
                (1 - gamma) * x_c[0] + gamma * x_r[0],
                (1 - gamma) * x_c[1] + gamma * x_r[1]
            ]
            f_e = f(x_e)
            if f_e < f_l:
                triangle[2] = x_e
            else:
                triangle[2] = x_r
            continue
        elif f_l<f_r<f_h:
            triangle[2] = x_r
        elif f_r > f_h:
            # сжатие
            x_k = [
                (1 - beta) * x_c[0] + beta * x_r[0],
                (1 - beta) * x_c[1] + beta * x_r[1]
            ]
            f_k = f(x_k)
            if f_k < f_h:
                triangle[2] = x_k
            else:
                # Редукция
                for i in range(3):
                    x_i = [
                        0.5*(triangle[i][0] - x_l[0]) + x_l[0],
                        0.5*(triangle[i][1] - x_l[1]) + x_l[1]
                    ]
                    triangle[i] = x_i
    return triangle[0], f(triangle[0]), k

if __name__ == '__main__':
    print("Метод Нелдера-Мида")
    x_min, f_min, n = Nerdera_Mida([0,0])
    print("Вектор х: ", x_min)
    print("Минимальное значение: ", f_min)
    print("Количество итераций", n)
    print()

    print("Метод Хука-Дживса")
    x_min, f_min, n = method_XDg([0, 0])
    print("Вектор х: ", x_min)
    print("Минимальное значение: ", f_min)
    print("Количество итераций", n)
