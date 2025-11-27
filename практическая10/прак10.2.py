filename_input = "C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vvod_2.txt"
filename_output = "C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vivod_2.txt"

with open(filename_input, 'r', encoding='utf-8') as file_1:
    lines = file_1.readlines()

matrix = []
for line in lines:
    line = line.strip()
    if line:
        i = list(map(int, line.split()))
        matrix.append(i)
        
for i in matrix:
    c = i[0]
    i[0] = i[-1]
    i[-1] = c

with open(filename_output, 'w', encoding='utf-8') as file_2:
    for i in matrix:
        file_2.write(' '.join(map(str, i)) + '\n')
