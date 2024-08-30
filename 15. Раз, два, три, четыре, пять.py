def calculate_structure_sum(data_structure):
    # Изначально устанавливаем сумму чисел и длину строк в 0
    total_sum = 0
    total_string_length = 0

    # Вложенная функция для прохода по элементам структуры
    def traverse(element):
        # Используем nonlocal для изменения переменной, которая находится в родительской области видимости
        nonlocal total_sum, total_string_length

        # Если элемент - число (int или float), добавляем его к общей сумме
        if isinstance(element, (int, float)):
            total_sum += element
        # Если элемент - строка, добавляем длину строки к общей длине строк
        elif isinstance(element, str):
            total_string_length += len(element)
        # Если элемент является коллекцией (list, tuple или set), рекурсивно вызываем traverse для каждого элемента
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                traverse(item)
        # Если элемент является словарем, рекурсивно вызываем traverse для ключей и значений
        elif isinstance(element, dict):
            for key, value in element.items():
                traverse(key)   # Проход по ключу
                traverse(value) # Проход по значению

    # Проходим по каждому элементу основной структуры
    for item in data_structure:
        traverse(item)

    # Возвращаем сумму чисел и длину строк
    return total_sum + total_string_length

# Пример использования функции
data_structure = [
    [1, 2, 3],                              # список с числами
    {'a': 4, 'b': 5},                       # словарь с числами в качестве значений
    (6, {'cube': 7, 'drum': 8}),            # кортеж с числом и словарем
    "Hello",                                 # строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # более сложная структура, содержащая пустой кортеж и список с множеством вложенных элементов
]

# Вызываем функцию с примером структуры и выводим результат
result = calculate_structure_sum(data_structure)
print(result)  # печатает результат
