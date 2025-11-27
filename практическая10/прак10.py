filename_input = 'C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vvod.txt'
filename_output = 'C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vivod.txt'

with open(filename_input, 'r', encoding='utf-8') as file_1:
    lines = file_1.readlines()

matrix = []
for line in lines:
    line = line.strip()
    if line:
        i = list(map(int, line.split()))
        matrix.append(i)

def magic(matrix):
    n = len(matrix)
    for i in matrix:
        if len(i) != n:
            return False
        
    sum_1 = sum(matrix[0])
    for i in matrix:
        if sum(i) != sum_1:
            return False
        
    for j in range(n):
        sum_2 = sum(matrix[i][j] for i in range(n))
        if sum_2 != sum_1:
            return False
    return True
    
with open(filename_output, 'w', encoding='utf-8') as file_2:
    if magic(matrix):
        file_2.write('матрица является магическим квадратом')
    else:
        file_2.write('матрица не является магическим квадратом')
