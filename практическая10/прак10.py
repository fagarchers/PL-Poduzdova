filename_input = 'C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vvod.txt'
filename_output = 'C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vivod.txt'

with open(filename_input, 'r', encoding='utf-8') as file_1:
    lines = file_1.readlines()

n = int(lines[0].strip())
a_lines = lines[1:]
a = []
for i in range(n):
    b = list(map(int, a_lines[i].strip().split()))
    a.append(b)
sum_1 = sum(a[0])
magic = True
for i in range(n):
    if sum(a[i]) != sum_1:
        magic = False
        break
for j in range(n):
        sum_2 = 0
        for i in range(n):
            sum_2 += a[i][j]
        if sum_2 != sum_1:
            magic = False
            break
        
with open(filename_output, 'w', encoding='utf-8') as file_2:
    if magic == True:
        file_2.write('матрица является магическим квадратом')
    else:
        file_2.write('матрица не является магическим квадратом')
