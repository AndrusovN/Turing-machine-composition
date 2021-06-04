path1 = input('Введите путь к первой МТ: ')
path2 = input('Введите путь ко второй МТ: ')

f1 = open(path1, 'r')
f2 = open(path2, 'r')

name = input('Введите название файла для сохранения результата: ')
f3 = open(name + '.txt', 'w')

states1 = -1
states2 = -1

for s1 in f1.readlines():
    if states1 == -1:
        states1 = s1.count('\t')
    s2 = f2.readline()[1:]
    if states2 == -1:
        states2 = s2.count('\t')
    for i in range(states2, 0, -1):
        s2 = s2.replace('>' + str(i) + '\t', '>' + str(i + states1) + '\t')
        s2 = s2.replace('.' + str(i) + '\t', '.' + str(i + states1) + '\t')
        s2 = s2.replace('<' + str(i) + '\t', '<' + str(i + states1) + '\t')
        s2 = s2.replace('>' + str(i) + '\n', '>' + str(i + states1) + '\n')
        s2 = s2.replace('.' + str(i) + '\n', '.' + str(i + states1) + '\n')
        s2 = s2.replace('<' + str(i) + '\n', '<' + str(i + states1) + '\n')
    print(s2)

    s1 = s1.replace('.0', '.' + str(states1 + 1))
    s1 = s1.replace('>0', '>' + str(states1 + 1))
    s1 = s1.replace('<0', '<' + str(states1 + 1))
    s = s1[:-1] + s2
    f3.write(s)


f1.close()
f2.close()
f3.close()