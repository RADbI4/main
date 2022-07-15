"""
Программа для вывода рабочих и выходных дней для людей, работающих 2/2
"""
import calendar

# month_weeks = calendar.monthcalendar(2022, 9)
def last_day_of_month(month):
    '''
    Возвращает последнее число месяца
    :param month:
    :return:
    '''
    last_day_of_month = []
    k = 0
    if len(month) == 5:
        k = 4
    elif len(month) == 6:
        k = 5
    for day in month_weeks[k]:
        if day >= 30:
            a = day
            last_day_of_month.append(a)
    if len(last_day_of_month) > 1 and last_day_of_month[0] + last_day_of_month[1] == 61:
        return 31
    elif len(last_day_of_month) == 1 and last_day_of_month[0] == 31:
        return 31
    elif len(last_day_of_month) == 1 and last_day_of_month[0] == 30:
        return 30

# print(month_weeks, last_day_of_month(month_weeks))

z = 7  # месяц, с которого начинается отчёт
month_weeks = calendar.monthcalendar(2022, z)
i = 5 # первое рабочее число
j = i +1  # второе рабочее число
work_days = []
month_name = list(calendar.month_name)
# print(month_name[z])
while z != 13:
    month_weeks = calendar.monthcalendar(2022, z)
    for week in month_weeks:
        for day in week:
            if day == i:
                if last_day_of_month(month_weeks) == 30 and i == 31:
                    break
                else:
                    work_days.append(i)
                i += 4
                if j != 32:
                    work_days.append(j)
                    j += 4
    print(f'Рабочие числа в {month_name[z]}')
    print(work_days)
    if last_day_of_month(month_weeks) == 31 and work_days[-1] == 31:
        i = 3
        j = i + 1
    elif last_day_of_month(month_weeks) == 31 and work_days[-1] == 30:
        i = 3
        j = i + 1
    elif last_day_of_month(month_weeks) == 31 and work_days[-1] == 29:
        i = 1
        j = i + 1
    elif last_day_of_month(month_weeks) == 30 and work_days[-1] == 29:
        i = 2
        j = i + 1
    elif last_day_of_month(month_weeks) == 30 and work_days[-1] == 28:
        i = 1
        j = i + 1
    else:
        print('Невозможно, пересмотри программу или входные данные')
    z += 1
    work_days.clear()


