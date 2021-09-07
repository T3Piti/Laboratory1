#Сумма трех
def Summ():
    first = int(input());
    second = int(input());
    third = int(input());
    summ = first + second + third;
    print('Сумма: ', summ);
#Площадь треугольника
def TriangleArea():
    height = float(input());
    base = float(input());
    area = (base * height) / 2;
    print('Площадь: ', area);
#Апельсины
def PartialRemainder():
    childrens = int(input());
    oranges = int(input());
    childOranges = oranges // childrens;
    remainengOranges = oranges % childrens;
    print('Апельсинов у ребенка: ', childOranges);
    print('Остаток: ', remainengOranges);
#Часы
def MinutesToHoursMinutes():
    minutes = int(input());
    hours = minutes // 60;
    minutes %= 60;
    print('Часы: ', hours, 'Минуты: ', minutes);
#Print hello + string
def StringMultiply():
    name = input();
    print('Hello, ', name , '!');
#Next and previous
def NextAndPrevious():
    number = int(input());
    print('The next number for the number %d is %d' % (number, number+1));
    print('The previous number for the number %d is %d' % (number, number-1));
#School desks
def ComputersCount():
    desks = 0;
    personsAtGroups = input().split();
    for item in personsAtGroups:
        if(int(item) % 2 != 0):
            item = int(item) + 1;
        desks +=int(item)/2;
    print('Необходимо %d парт' % desks);
#laces
def GetLaceLength():
    horizontal = int(input());
    vertical = int(input());
    freeLength = int(input());
    holesQuantity = int(input());
    laceLength = (horizontal+vertical) * 2 * (holesQuantity-1) + freeLength * 2 + horizontal;
    print('Длинна шнурка: %d' % laceLength);