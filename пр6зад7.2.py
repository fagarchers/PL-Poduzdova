a = list(map(int,input('введите массив:').split()))
print('изначальный массив:',a)
minimum = min(a)
maximum = max(a)
index_min = a.index(minimum)
index_max = a.index(maximum)
b = a[index_min]
a[index_min] = a[index_max]
a[index_max] = b
print('новый массив', a)
