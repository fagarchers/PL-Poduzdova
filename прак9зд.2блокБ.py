def finding_second_maximum(n, first_maximum=0, second_maximum=0):
   if not n:
       return second_maximum
   a = n[0]
   if a > first_maximum:
       second_maximum = first_maximum
       first_maximum = a
   elif a > second_maximum and a != first_maximum:
       second_maximum = a
   return finding_second_maximum(n[1:], first_maximum, second_maximum)
massive = []
while True:
    c = int(input('введите число:'))
    if c == 0:
        break
    massive.append(c)
answer = finding_second_maximum(massive)
print('значение второго по величине максимума:', answer)
    
