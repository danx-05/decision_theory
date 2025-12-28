import numpy as np
def transport_potentials(a, b, C):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    C = np.array(C, dtype=float)
    m, n = len(a), len(b)
    X = np.zeros((m, n))
    i, j = 0, 0
    supply = a.copy()
    demand = b.copy()
    while i < m and j < n:
        quantity = min(supply[i], demand[j])
        X[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity
        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1
    iteration = 0
    while iteration < 100:
        iteration += 1
        basis = [(i, j) for i in range(m) for j in range(n) if X[i, j] > 0]
        print(X)
        if len(basis) < m + n - 1:
            for i in range(m):
                for j in range(n):
                    if X[i, j] == 0 and (i, j) not in basis:
                        basis.append((i, j))
                    if len(basis) == m + n - 1:
                        break
                if len(basis) == m + n - 1:
                    break
        print(basis)
        u = np.full(m, np.nan)
        v = np.full(n, np.nan)
        u[0] = 0
        changed = True
        while changed:
            changed = False
            for i, j in basis:
                if not np.isnan(u[i]) and np.isnan(v[j]):
                    v[j] = C[i, j] + u[i]
                    changed = True
                elif np.isnan(u[i]) and not np.isnan(v[j]):
                    u[i] = - C[i, j] + v[j]
                    changed = True

        min_delta = 0
        min_x = None

        Delta = np.zeros_like(X)
        for i in range(m):
            for j in range(n):
                if (i, j) not in basis:
                    delta = C[i, j] - (v[j] - u[i])
                    Delta[i,j] = delta
                    if delta < min_delta:
                        min_delta = delta
                        min_x = (i, j)
        if min_x is None:
            break
        print(Delta)

        i0, j0 = min_x

        visited = set()
        path = []
        signs = []

        def find_cycle_dfs(i, j, last_move='row', current_path=None, current_signs=None):
            if current_path is None:
                current_path = [(i, j)]
                current_signs = ['+']
            if len(current_path) > 3 and (i, j) == (i0, j0):
                return current_path, current_signs

            visited.add((i, j))
            if last_move == 'row':
                for ii in range(m):
                    if ii != i and (X[ii, j] > 0 or (ii == i0 and j == j0)):
                        if (ii, j) not in visited or (ii == i0 and j == j0):
                            next_sign = '-' if current_signs[-1] == '+' else '+'
                            result = find_cycle_dfs(ii, j, 'col',
                                                    current_path + [(ii, j)],
                                                    current_signs + [next_sign])
                            if result is not None:
                                return result
            else:
                for jj in range(n):
                    if jj != j and (X[i, jj] > 0 or (i == i0 and jj == j0)):
                        if (i, jj) not in visited or (i == i0 and jj == j0):
                            next_sign = '-' if current_signs[-1] == '+' else '+'
                            result = find_cycle_dfs(i, jj, 'row',
                                                    current_path + [(i, jj)],
                                                    current_signs + [next_sign])
                            if result is not None:
                                return result
            visited.remove((i, j))
            return None
        result = find_cycle_dfs(i0, j0, 'row')
        if result is None:
            basis.append((i0, j0))
            continue

        cycle, signs = result

        theta = float('inf')
        min_cell = None
        for idx, ((i, j), sign) in enumerate(zip(cycle[1:], signs[1:])):
            if sign == '-' and X[i, j] < theta:
                theta = X[i, j]
                min_cell = (i, j)

        if theta == 0:
            theta = 10 ** (-6)

        for idx, ((i, j), sign) in enumerate(zip(cycle, signs)):
            if idx == 0:
                continue
            if sign == '+':
                X[i, j] += theta
            else:
                X[i, j] -= theta

        X[i0, j0] = theta
        X[X < 1e-9] = 0.0

    total_cost = np.sum(X * C)
    return X, total_cost
a = [60, 70, 20]
b = [40, 30, 30, 50]
C = np.array([
    [2, 4, 5, 1],
    [2, 3, 9, 4],
    [3, 4, 2, 5]
])

X, cost = transport_potentials(a, b, C)
print("\nОптимальный план перевозок:")
print(X)
print(f"\nМинимальная стоимость: {cost}")