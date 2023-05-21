def rifma(chant):
    st = chant.lower().split()
    print(st)
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(st[0])
    if all([f(i) == tmp for i in st]):
        return 'Парам пам-пам'
    return 'Пам парам'

print(rifma(input("Введите стих ")))