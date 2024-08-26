def calculate_structure_sum(data):
    total_sum = 0

    # Проверяем тип элементов
    for element in data:
        if isinstance(element, (int, float)):  # Если элемент число
            total_sum += element
        elif isinstance(element, str):  # Если элемент строка
            total_sum += len(element)
        elif isinstance(element, list):  # Если элемент список
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов
        elif isinstance(element, dict):  # Если элемент словарь
            total_sum += calculate_structure_sum(element.items())  # Рекурсивный вызов со словарем
        elif isinstance(element, tuple):  # Если элемент кортеж
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99