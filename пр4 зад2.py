a = int(input('Введите целое число a:'))
b = int(input('Введите целое число b:'))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
