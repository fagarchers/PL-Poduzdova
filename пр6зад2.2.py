a = list(map(int,input('введите массив целых чисел:').split()))
positive = []
negative = []
for i in a:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print('положительные:', positive)
print('остальные:', negative)
