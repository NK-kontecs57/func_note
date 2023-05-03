def y_n():
    for i in range(100):
        result = {}
        name = input('Введите свое имя и фамилию:')
        height = int(input('Введите свой рост(в см):'))
        ans = ('годен' if height < 170 else 'не годен')
        print(ans)
        result[name] = ans
        s = input('Хотите продолжить программу(да, нет):')
        if s.upper() == 'НЕТ':
            break
        return result
print(y_n())
