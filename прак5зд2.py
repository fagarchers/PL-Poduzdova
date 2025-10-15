s = input('введите текст с двоеточием:')
k = s.count(':')
s = s.replace(':','%')
print(s,k,sep='\n')

