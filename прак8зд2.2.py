n = int(input('введите размер матрицы:'))
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('введите [', i, ',', j, ']элемент:')
        b.append(int(input()))
    a.append(b)
print('изначальный массив:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    c = a[i][0]
    a[i][0] = a[i][n-1]
    a[i][n-1] = c
print('новый массив:')
for b in a:
    print(b)



