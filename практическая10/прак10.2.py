filename_input = "C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vvod_2.txt"
filename_output = "C:\практическая10\Подуздова Юлия Викторовна_УБ-51_vivod_2.txt"

with open(filename_input, 'r', encoding='utf-8') as file_1:
    lines = file_1.readlines()
    
n = int(lines[0].strip())
a_lines = lines[1:]
a = []
for i in range(n):
    b = list(map(int, a_lines[i].strip().split()))
    a.append(b)
for i in range(n):
    c = a[i][0]
    a[i][0] = a[i][n-1]
    a[i][n-1] = c
    
with open(filename_output, 'w', encoding='utf-8') as file_2:
    for b in a:
        file_2.write(' '.join(map(str, b)) + '\n')
