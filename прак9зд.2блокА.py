def s(a, b):
    if a < b:
        return a
    else:
        return s(a - b, b)
a = int(input('a: '))
b = int(input('b: '))
print('остаток от деления a на b:', s(a, b))


    
