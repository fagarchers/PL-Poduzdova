import math
def S_triangle(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p*(p - a)*(p - b)*(p - c))
def S_hexagon(a):
    s_triangle = S_triangle(a, a, a)
    return 6 * s_triangle
a = float(input('введите длину стороны шестиугольника:'))
S = S_hexagon(a)
print('площадь правильного шестиугольника равна:', S)
