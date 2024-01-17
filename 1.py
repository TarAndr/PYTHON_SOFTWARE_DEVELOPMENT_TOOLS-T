# Функция для выполнения операции сложения
def add(x, y):
    return x + y

# Функция для выполнения операции вычитания
def subtract(x, y):
    return x - y

# Функция для выполнения операции умножения
def multiply(x, y):
    return x * y

# Функция для выполнения операции деления
def divide(x, y):
    # Добавим проверку деления на ноль
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"

# Запрос у пользователя двух чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вывод меню операций
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Запрос у пользователя выбора операции
choice = input("Введите номер операции (1/2/3/4): ")

# Выполнение выбранной операции и вывод результата
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Неверный ввод. Пожалуйста, выберите операцию снова.")
