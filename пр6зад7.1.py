a = list(map(int,input('введите массив целых чисел:').split()))
sum1 = 0
pro = 1
for i in range(len(a)):
    if i % 2 == 0:
        sum1 += a[i]
    else:
        pro *= a[i]
print('сумма:', sum1)
print('произведение:', pro)
