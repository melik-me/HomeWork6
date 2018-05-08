# Задание 5 * (доп.)
#
# Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата(В первой строке заголовки
# колонок)
# Посчитайте сколько отделов на фирме
# Определите максимальную зарплату
# Определите максимальную зарплату в каждом отделе
# Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в новый файл

l = []
with open("employees.txt") as f:
    for line in f:
        l.append(line.split())

keys = l[0]
l.pop(0)

employees = []
for item in l:
    d = {keys[0]: item[0], keys[1]: item[1], keys[2]: item[2], keys[3]: item[3]}
    employees.append(d)

departments = []
max_salary = 0

for employee in employees:
    if employee['Department'] not in departments:
        departments.append(employee['Department'])
    if int(employee['Salary']) > max_salary:
        max_salary = int(employee['Salary'])

print("Company consists of {} departments.".format(len(departments)))
print("Maximum salary is {}.\n".format(max_salary))

lucky_list = []
for department in departments:
    d = {'department': department, 'salary': 0, 'surname': ''}
    lucky_list.append(d)


for employee in employees:
    for lucky in lucky_list:
        if employee['Department'] == lucky['department'] and int(employee['Salary']) > lucky['salary']:
            lucky['salary'] = int(employee['Salary'])
            lucky['surname'] = employee['Surname']

for lucky in lucky_list:
    print("Maximum salary in {} department is {}.".format(lucky['department'], lucky['salary']))

with open("Lucky_list.txt", "w") as f:
    for lucky in lucky_list:
        print("{} {} {}".format(lucky['department'], lucky['salary'], lucky['surname']), file=f)