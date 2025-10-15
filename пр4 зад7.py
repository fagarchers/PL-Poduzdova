n = int(input('введите значение n:'))
first_sum = 0
first_factorial = 1
for i in range(1, n+1):
    first_factorial = first_factorial*i
    first_sum = first_sum+first_factorial
print(first_sum)
