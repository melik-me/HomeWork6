# Задание 3
#
# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
#
# * (доп.) Рядом со словом укажите сколько раз оно встречалось в тексте

l = []

with open("Cicero.txt") as f:
    for line in f:
        l.append(line.split())

words = []
for list in l:
    for item in list:
        words.append(item.strip("""~`!@#$%^&*()_+-=[]{};':"/?.,><""").lower())

words.sort()

with open("alphabet.txt", "w") as f:
    while words:
        word = words[0]
        print(words.count(word), word, file=f)
        for i in range(words.count(word)):
            words.remove(word)

