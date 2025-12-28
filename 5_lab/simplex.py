import numpy as np

M = 10 ** 6

F = [3, -2]

c =[
    [2, 1],
    [-3, 2],
    [3, 4]
    ]
sign = ["<", "<",">"]
b = [11, 10, 20]

c_i = [0, -3, 2]
l = 0
for i in range(len(sign)):
    if sign[i] == "<":
        l+=1
    else:
        l += 2
L = [[0] * l for i in range(len(b))]

k = 0
mn = []
for i in range(len(sign)):
    if sign[i] == "<":
        L[i][k] = 1
        k+=1
        mn.append(0)
        c_i.append(0)
    else:
        L[i][k] = -1
        c_i.append(0)
        L[i][k+1] = 1
        c_i.append(M)
        k += 2
        mn.append(-M)
print(c_i)
table = []
for i in range(len(b)):
    a = [b[i], c[i][0], c[i][1]]
    for j in L[i]:
        a.append(j)

    table.append(a)
f = []
for i in range(len(table[0])):
    summ = 0
    for j in range(len(table)):
        summ += table[j][i] * mn[j]
    summ += c_i[i]

    f.append(summ)

initial_t = []
initial_t.append(f)
for i in range(len(table)):
    initial_t.append(table[i])
print(initial_t)
initial_table = np.array(initial_t, dtype=float)

def get_pivot_row(table, pivot_col_index):
    min_ratio = float('inf')
    min_indices = []

    for i in range(1, len(table)):
        if table[i][pivot_col_index] > 0:
            ratio = table[i][0] / table[i][pivot_col_index]
            if ratio < min_ratio:
                min_ratio = ratio
                min_indices = [i]
            elif abs(ratio - min_ratio) < 10 ** (-8):
                min_indices.append(i)
    if not min_indices:
        raise ValueError("Решение недостижимо: задача не ограничена")
    pivot_row_index = max(min_indices)
    return pivot_row_index

def update_tableau(table, pivot_row_index, pivot_col_index):
    n_rows, n_cols = table.shape
    result_table = np.zeros_like(table, dtype=float)

    pivot_element = table[pivot_row_index][pivot_col_index]
    for j in range(n_cols):
        result_table[pivot_row_index][j] = table[pivot_row_index][j] / pivot_element

    for i in range(n_rows):
        if i == pivot_row_index:
            continue
        for j in range(n_cols):
            result_table[i][j] = table[i][j] - table[i][pivot_col_index] * result_table[pivot_row_index][j]

    return result_table

basis_indices = []
current_table = initial_table.copy()
iteration = 0
print("Начальная таблица:")
print(current_table)

while np.any(current_table[0, 1:] < 0):
    iteration += 1
    print(f"\n--- Итерация {iteration} ---")
    pivot_col_index = np.argmin(current_table[0, 1:]) + 1
    try:
        pivot_row_index = get_pivot_row(current_table, pivot_col_index)
    except ValueError:
        print("Оптимальное решение недостижимо: задача не ограничена.")
        break

    print(f"Разрешающий столбец: {pivot_col_index}, строка: {pivot_row_index}")
    basis_indices.append((pivot_row_index, pivot_col_index))
    current_table = update_tableau(current_table, pivot_row_index, pivot_col_index)
    print("Таблица после пересчета:")
    print(current_table)

print("Итоговые результаты:")

for row_idx, col_idx in basis_indices:
    if col_idx in [1, 2]:
        value = current_table[row_idx][0]
        print(f"x{col_idx} = {value:.2f}")

optimal_F = current_table[0][0]
print(f"Значение целевой функции F(x) = {optimal_F:.2f}")