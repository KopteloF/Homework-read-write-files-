file_for_writing = []
file_count = 1
sum_line = {}

while file_count <= 3:
    file_name = f'{file_count}.txt'
    with open(file_name, 'rt', encoding='utf-8') as f:
        file_oneline = []
        counting = 0
        for line in f.readlines():
            file_oneline.append(line)
            counting += 1
        sum_line[file_name] = file_oneline
    file_count += 1

sorted_dict = dict(sorted(sum_line.items(), key=lambda x: len(x[1])))
for key, value in sorted_dict.items():
    file_for_writing += value

print(sorted_dict)

with open('sorted_dict_file.txt', 'x', encoding='utf-8') as f:
    for key, value in sorted_dict.items():
        f.write(str(key) + '\n')
        f.write(str(len(value)) + '\n')
        f.write(''.join(value))
        f.write('\n')