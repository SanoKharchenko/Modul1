mass = 4.5
price = 34
money = int(input('Введите количество денег: '))
print(int(money-mass*price))

price1 = int(input('Введите цену товара: '))
mass1 = int(input('Введите массу товара: '))
money1 = int(input('Введите количество денег: '))
print(int(money1-mass1*price1))

name = input('Введите название товара : ')
price2 = int(input('Цена товара : '))
mass2 = int(input('Вес товара : '))
money2 = int(input('Денег получено : '))
sdacha = int(money2-mass2*price2)
print('Чек')
print(name, mass2, 'кг', price2, 'руб/кг')
print('Итого: ',int(mass2*price2),'руб')
print('Внесено: ',money2, 'руб')
print('Сдача: ',sdacha,'руб')

n = int(input('Количество сторк '))
print('Купи конструктор'*n)

