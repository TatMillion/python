# author = Миллионщикова Татьяна Дмитриевна
# 1

first_list = []

first_list.append(2)
first_list.append('str')
first_list.append(15.6)
first_list.append(None)
first_list.append(False)

print(first_list)
for el in first_list:
    print(type(el))

# 2
m = [int(i) for i in input().split()]
for i in range(1, len(m), 2):
    m[i - 1], m[i] = m[i], m[i - 1]
print(' '.join(str(i) for i in m))

# 3
### решение через словарь
month = int(input('введите месяц'))
seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', \
      9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(f' This month is connected to {seasons.get(month)}')
### решение через список
month_new = int(input('введите месяц'))
seasons_new = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', \
             'autumn', 'winter']
print(f'This month is connected to {seasons_new[month_new-1]}')

#4
line = input('введите строку')
words = line.split()
for ix, word in enumerate(words):
    if len(word) > 10:
        print(f'{ix} {word[0:9]}')
    else:
        print(f'{ix} {word[0:9]}')

#5
my_list = [7, 5, 3, 3, 2]
num = int(input('введите число'))
if num > max(my_list):
    my_list.insert(0, num)
elif num < min(my_list):
    my_list.insert(len(my_list), num)
else:
    for el in my_list:
        print(el)
        if num <= el:
            continue
        else:
            my_list.insert(my_list.index(el), num)
            break
print(my_list)

#6
gds_list = []
while True:
    gd_no = int(input('Введите номер товара: \n'))
    gd_name = input('Введите название товара: \n')
    gd_cost = int(input('Введите цену товара: \n'))
    gd_num = int(input('Введите количество товара: \n'))
    gd_ed = input('Введите единицу измерения товара: \n')
    gds_list.append((gd_no, {'название': gd_name, 'цена': gd_cost, 'количество': gd_num, 'eд': gd_ed}))
    cont = input('Закончить? (да/нет): \n')
    if cont == 'да':
        break
    elif cont == 'нет':
        continue
    else:
        print('Вы ввели неправильный ответ. Цикл будет продолжен')
        continue
print(gds_list)
names_list = []
cost_list = []
num_list = []
qnt_list = []
for good in gds_list:
    data_dict = good[1]
    names_list.append(data_dict.get('название'))
    cost_list.append(data_dict.get('цена'))
    num_list.append(data_dict.get('количество'))
    qnt_list.append(data_dict.get('eд'))
final_dict = {'название': names_list, 'цена': cost_list, 'количество': num_list, 'eд': qnt_list}
print(final_dict)