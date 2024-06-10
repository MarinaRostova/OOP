sum_line =[]

with open('1.txt', encoding="utf8") as file1:
    f1=file1.readlines()
    line_1 = len(f1)
    sum_line.append(['1.txt',line_1, f1])

with open('2.txt', encoding="utf8") as file2:
    f2=file2.readlines()
    line_2 = len(f2)
    sum_line.append(['2.txt', line_2, f2])

with open('3.txt', encoding="utf8") as file3:
    f3 = file3.readlines()
    line_3 = len(f3)
    sum_line.append(['3.txt', line_3, f3])

print(line_1)
print(line_2)
print(line_3)

sum_line.sort(key=lambda item: item[1])
print(sum_line)