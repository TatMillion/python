#  1
with open('my_file.txt', 'w', encoding='utf-8') as f:
    while True:
        f_new = input('введите строку')
        if f_new == '':
            break
        f.writelines(f_new+'\n')
print('конец')

#  2
with open('my_file2.txt.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'Количество строк {len(lines)}')
    for i, line in enumerate(lines):
        print(f'Количество слов в строке {i+1}:{len(line.split())}')

# 3
with open('text_3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # read all lines
    sals = []  # list to save salaries
    for line in lines:
        if float(line.split()[1]) < 20000:
            print(f'The salary of {line.split()[0]} is less than 20K RUB')
        sals.append(float(line.split()[1]))
print(f'Mean salary is {sum(sals) / len(sals)}')

# 4
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
with open('text_4.txt', 'r', encoding='utf-8') as eng_dict:
    words = eng_dict.readlines()
    for word in words:
        wls = word.split(' -')
        print(wls)
        wls[0] = translator.get(wls[0])
        print(wls)
        my_list.append(wls[0] + ' -' + str(wls[1]))
with open('text_4_new.txt', 'w', encoding='utf-8') as f_new:
    f_new.writelines(my_list)

# 5
with open('my_file_5.txt', 'w', encoding='utf-8') as f:
    new_number = input('введите строку')
    f.writelines(new_number)
    print(sum([float(n) for n in new_number.split()]))

# 6
sbj_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        items = line.split(':')
        toth = sum([int(el) for el in (''.join([sym if sym.isdigit() else ' ' for sym in items[1]])).split(' ') if el != ''])
        print(toth)
        sbj_dict.update({items[0]:toth})
print(sbj_dict)

# 7
firm_dict = {}
prb = []
fin_ls = []
with open('text_7.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        items = line.split()
        if float(items[2])-float(items[3])>=0:
            prb.append(float(items[2])-float(items[3]))
        firm_dict.update({items[0]:(float(items[2])-float(items[3]))})
        #toth = sum([int(el) for el in (''.join([sym if sym.isdigit() else ' ' for sym in items[1]])).split(' ') if el != ''])
        #print(toth)
        #sbj_dict.update({items[0]:toth})
fin_ls.append(firm_dict)
fin_ls.append({"average_profit":sum(prb)/len(prb)})
print(fin_ls)
import json
with open('text_7_fin.json', 'w') as f:
    json.dump(fin_ls, f)

