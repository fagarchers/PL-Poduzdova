n = int(input('введите порядок матрицы:'))
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('введите [', i,',', j,'] элемент:')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
sum_1 = sum(a[0])
magic = True
for i in range(n):
    if sum(a[i]) != sum_1:
        magic = False
        break
for j in range(n):
    sum_2 = 0
    for i in range(n):
        sum_2 += a[i][j]
    if sum_2 != sum_1:
        magic = False
        break
if magic == True:
    print('матрица является магическим квадратом')
else:
    print('матрица не является магическим квадратом')
