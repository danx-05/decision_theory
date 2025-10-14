import numpy as np
import matplotlib.pyplot as plt

# Коэффициенты разностного уравнения: y[n] = a*y[n-1] + b*y[n-2] + c
a = 2    # Коэффициент при y[n-1]
b = 0    # Коэффициент при y[n-2]


c = 0   # Свободный член (постоянная составляющая)

# Начальные условия
y0 = 0    # y[0]
y1 = 1     # y[1]

# Параметры расчета
N = 10  # Количество вычисляемых точек

# Инициализация массива решений
y = np.zeros(N)
y[0] = y0
y[1] = y1

# Вычисление решения разностного уравнения
for n in range(2, N):
    y[n] = a * y[n-1] + b * y[n-2] + c

# Построение графика
plt.figure(figsize=(6, 6))
plt.plot(y, 'b.', markersize=10)
plt.xlabel('n', fontsize=12)
plt.ylabel('y[n]', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, N)
plt.tight_layout()
plt.show()

# Дополнительно: вывод первых 10 значений для проверки
print("Первые 10 значений решения:")
for i in range(10):
    print(f"y[{i}] = {y[i]:.4f}")