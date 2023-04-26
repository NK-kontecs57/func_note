def sum_numbers():
    s = 'нет'
    while s.lower() != 'да':
        numbers_lst = [int(i) for i in input('Введите числа через пробел:').split()]
        print(sum(numbers_lst))
        s = input('Вы хотите завершить программу("да" или "нет"):')
sum_numbers()