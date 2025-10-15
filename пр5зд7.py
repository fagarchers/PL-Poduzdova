s = input('Введите строку с буквой п:')
n = len(s)
n1 = n//2
s1 = s[:n1].replace('п','*')
s = s1+s[n1:]
print(s)
