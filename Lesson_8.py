# =====#1=====

class x():

    def __init__(self, d, m, y):
        self.d, m, y = d, m, y

    @classmethod
    def operator(что_то, r):
        try:
            d, m, y = map(int, r.split("-"))

            if d <= 31 and d != 0 and m <= 12 and m != 0:
                print(r)
            else:
                return x.if_error_date()
        except ValueError:
            return x.if_error()

    def if_error(): #отсутствие @staticmethod не ломает конструкцию =D
        print("Неравильный ввод знака разделения дат!")

    def if_error_date():
        print("Неравильный ввод даты")

d,m,y = '01','04','2020'
m1 = '40'
z = '-'
z1 = '/'

x.operator(d + z + m + z + y)
x.operator(d + z + m1 + z + y)
x.operator(d + z1 + m + z + y)

# =====#2=====

class zero():

    def __init__(self, x,y):
        self.x,y = x,y

    @staticmethod
    def operator(x,y):
        try:
            print(int(x) / int(y))
        except ZeroDivisionError:
            return zero.if_error()

    @staticmethod
    def if_error():
        print("На ноль не делят! Но если Вы настаиваете то ответ равен: 42!")

x,y = input("введите первое число"),input("введите делитель не равный нулю!")
zero.operator(x,y)

# =====#3=====

class x():

    def __init__(self,*args):
        self.s = []

    def control(self):

        while True:
            try:
                y = input('введите числа и "enter". Для выхода нажмите "q":')
                if y == 'q':
                    return print(f"Ваш итоговый список: {self.s}")

                self.s.append(int(y))

            except:
                print(f"Не корректное значение! Продолжайте или нажмите выход 'q'")

x().control()

# =====#4-6=====

class Storage:

    def __init__(self, name, cat, price, total, number, *args):
        self.name = name
        self.cat = cat
        self.price = price
        self.total = total
        self.number = number
        self.sp = {}
        self.sp_full = []
        self.copir = []
        self.scan = []
        self.my_unit = {'Модель': self.name, 'Категория': self.cat, 'Цена': self.price, 'Количество': self.total}

    def __str__(self):
        return f'{self.name} категория: {self.cat} цена {self.price} количество {self.total}'

    def oper(self):

        while True:
            try:
                x = input(f'Введите наименование ')
                x1 = input(f'Введите категорию ')
                y = int(input(f'Введите цену за ед '))
                z = int(input(f'Введите количество '))
                un = {'Модель': x, 'Категория': x1, 'Цена': y, 'Количество': z}

                self.my_unit.update(un)
                self.sp.update(self.my_unit)
                self.sp_full.append(self.sp)
#                print(f'товар: -\n {self.sp_full}')

                if self.sp["Категория"] == 'copir':
                    self.copir.append(self.sp["Количество"])
                    print(f'Копиры: -\n {sum(self.copir)}')
                    print(f'Сканы: -\n {sum(self.scan)}')

                elif self.sp["Категория"] == 'scan':
                    self.scan.append(self.sp["Количество"])
                    print(f'Копиры: -\n {sum(self.copir)}')
                    print(f'Сканы: -\n {sum(self.scan)}')

                else: print(f'иная категория')

            except:
                break

class Copire(Storage):
    def to_copir(self):
        return f'итого на теперь на складе {self.total + sum(self.copir)} шт.'

class Scane(Storage):
    def to_scan(self):
        return f'итого на теперь на складе {self.total + sum(self.scan)} шт.' #Не понимаю почему одновременно
        # не работает, могу или первый или второй класс запускать, если одновременно sum(self.scan) нулевой

n=5
n1,n2 = 'Copire','Scane'

i = Scane('-', '-' , '-', n, '-')
print(i.oper())
print(i.to_scan())


# =====#7=====

class compl():

    def __init__(self, x, y, *args):
        self.x = x
        self.y = y

    def __add__(self, other):
        return print(f'comple add = {self.x + other.x} + {self.y + other.y}j')

    def __mul__(self, other):
        return print(f'comple mul = {self.x * other.x - (self.y * other.y)} + {self.y * other.x}j')

compl(100, 0.01) + compl(100, -0.01)
compl(100, 0.01) * compl(100, -0.01)