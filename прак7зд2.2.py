def s(a,b):
    s = a*b
    return s
A = []
for i in range(3):
    print('введите стороны', i, '- го прямоугольника:')
    a = int(input('сторона a:'))
    b = int(input('сторона b:'))
    A.append(s(a,b))
for i in range(3):
    print('площадь', i, '- го прямоугольника:', A[i])
    
    
