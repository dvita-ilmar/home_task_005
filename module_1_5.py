'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №5
Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
'''
# Задание кортежа
immutable_var = (34, 'python', 3.14, True, [1,2,3])
print(f'Кортеж: {immutable_var}')

print('\nimmutable_var[0] = 35 - выдается ошибка:')
print("TypeError: 'tuple' object does not support item assignment")
print('Кортежи нельзя изменять, потому что они были разработаны таким образом - когда требуется работать с массивом констант')

# Задание списка
mutable_list =  [34, 'python', 3.14, True, (1,2,3)]
print(f'\nИсходный список: {mutable_list}')
# Изменение элементов списка
mutable_list[0] = (1,2,3)
mutable_list[1] = False
mutable_list[2] = 5
mutable_list[3] = 23.67690923
mutable_list[4] = [10]
print(f'Измененный список: {mutable_list}')