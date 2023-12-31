import match
# Switch Case

"""
1. Дано целое число K. Вывести строку-описание оценки, соответствующей числу K
    (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """


k = 4

match k:
    case 1:
        print(f'{1} - "плохо"')
    case 2:
        print(f'{2} - "неудовлетворительно"')
    case 3:
        print(f'{3} - "удовлетворительно"')
    case 4:
        print(f'{4} - "хорошо"')
    case 5:
        print(f'{5} - "отлично"')
    case _:
        print("Ошибка")

"""
2. Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). 
    Определить количество дней в этом месяце для невисокосного года.
    """

number_month = 2

match number_month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f'В этом месяце всегда 31 день')
    case 2:
        print(f'В этом месяце невисокосного года 28 дней')
    case 4 | 6 | 9 | 11:
        print(f'В этом месяце всегда 30 дней')


"""
3. Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года.
    Вывести значения D и M для даты, следующей за указанной.
    """

d = 30
m = 1

match d and m:
    case n if d == 28 and m == 2:
        print(f'На следующий день наступит 1.{m + 1}')
    case n if 1 <= d <= 29 and 1 <= m <= 12:
        print(f'На следующий день наступит {d+1}.{m}')
    case n if d == 30 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        print(f'На следующий день наступит {d+1}.{m}')
    case n if d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        print(f'На следующий день наступит 1.{m + 1}')
    case n if d == 30 and (m == 4 or m == 6 or m == 9 or m == 11):
        print(f'На следующий день наступит 1.{m + 1}')
    case _:
        print("Какой-нибудь день наступит...")


"""
4. Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток)
    и принимать три цифровые команды:
0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
Дан символ C — исходное направление робота и целое число N — посланная ему команда. 
Вывести направление робота после выполнения полученной команды.
"""

direction = {"С": "север", "З": "запад", "Ю": "юг", "В": "восток"}
travel = {"0": "продолжать движение", "1": "поворот налево", "-1": "поворот направо"}


def robot(c, n):
    n = str(n)
    match robot:
        case a if c in direction and n in travel:
            return f"Робот движется на {direction.get(c)}, {travel.get(n)}. "
        case _:
            return f'Что-то не так с вводом данных...'

print(robot('Ю', -1))


"""
5. Дано целое число в диапазоне 100–999. 
    Вывести строку-описание данного числа, 
    например: 256 — «двести пятьдесят шесть», 
    814 — «восемьсот четырнадцать»."""


dict_utils = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть",
           "7": "семь", "8": "восемь", "9": "девять", "10": "десять"}

dict_tens = {"1": "десять", "2": "двадцать", "3": "тридцать", "4": "сорок", "5": "пятьдесят",
                "6": "шестьдесят", "7": "семьдесят", "8": "восемьдесят",
                "9": "девяносто"}

dict_hunderd = {"1": "сто", "2": "двести", "3": "триста", "4": "четырест", "5": "пятьсот",
                "6": "шестьсот", "7": "семьсот", "8": "восемьсот",
                "9": "девятьсот"}

# вариант 1
number = 900

match number:
    case a if len(str(a)) == 3 and a % 100 == 0:
        print(dict_hunderd.get(str(a//100)))
    case a if len(str(a)) == 3 and a // 10 % 10 == 0 and a % 10 != 0:
        print(dict_hunderd.get(str(a//100)), dict_utils.get(str(a % 10)))
    case a if len(str(a)) == 3 and a % 10 == 0:
        print(dict_hunderd.get(str(a//100)), dict_tens.get(str(a // 10 % 10)))
    case a if len(str(a)) == 3 and a % 100 != 0:
        print(dict_hunderd.get(str(a//100)), dict_tens.get(str(a // 10 % 10)), dict_utils.get(str(a % 10)))

    case _:
        print("Что-то не так...")


# вариант 2
int_number = 904
int_number_ = str(int_number)

my_list = []
for i in int_number_:
    my_list.append(i)

match my_list:
    case a if len(a) == 3 and a[0] in dict_hunderd and a[1] in dict_tens and a[2] in dict_utils:
        print(dict_hunderd.get(a[0]), dict_tens.get(a[1]), dict_utils.get(a[2]))
    case a if len(a) == 3 and a[0] in dict_hunderd and a[1] == "0" and a[2] == "0":
        print(dict_hunderd.get(a[0]))
    case a if len(a) == 3 and a[0] in dict_hunderd and a[1] in dict_tens and a[2] == "0":
        print(dict_hunderd.get(a[0]), dict_tens.get(a[1]))
    case a if len(a) == 3 and a[0] in dict_hunderd and a[1] == "0" and a[2] in dict_utils:
        print(dict_hunderd.get(a[0]), dict_utils.get(a[2]))
    case _:
        print("Что-то не так...")


"""
6.    *** Реализуйте программу калькулятор. 
    На вход подается три значения: первое число, 
    второе число и операция( *, /, + или -) . 
    На выходе должны получить число, после выполнения операции.
    """

def calculator(a, b, operation):
    match operation:
        case '*':
            return a * b
        case '/':
            return round(a / b, 2)
        case '+':
            return a + b
        case '-':
            return a - b

print(calculator(5, 3, '*'))
