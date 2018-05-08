# Задание 2
# Задание из класса «Записываем “Number: строка из файла” из одного файла в другой»

r = open("Cicero.txt")
i = 1
with open("numered_write.txt", "w") as w:
    for line in r:
        w.write(str(i) + ": " + line)
        i += 1

r.seek(0)
i = 1
with open("numered_print.txt", "w") as w:
    for line in r:
        print(str(i) + ": " + line.rstrip(), file=w)
        i += 1

r.close()