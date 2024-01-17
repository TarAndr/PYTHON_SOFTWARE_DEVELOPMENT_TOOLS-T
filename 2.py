import random

# Генерация случайного списка
random_list = [random.randint(1, 100) for _ in range(10)]

# Имя файла для сохранения списка
file_name = "random_list.txt"

# Запись списка в текстовый файл
with open(file_name, "w") as file:
    for number in random_list:
        file.write(str(number) + "\n")

print(f"Список сохранен в файле {file_name}")