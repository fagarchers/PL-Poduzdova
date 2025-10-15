n = int(input('введите количество элементов:'))
list = []
for i in range(n):
    el = int(input('элемент '+str(i)+':'))
    list.append(el)
minimum = min(list)
index_min = list.index(minimum)
print('минимальный элемент:', minimum)
print('индекс минимального элемента:', index_min)
