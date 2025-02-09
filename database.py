def get_variant(variant_number):
    """
    Возвращает переменные для указанного варианта.
    """
    if 1 <= variant_number <= len(variants):
        return variants[variant_number - 1]
    else:
        raise ValueError("Недопустимый номер варианта")
    

variants = [
    {    "a1": 3, "a2": 5, "a3": 8, "n1": 16, "n2": 11, "n3": 13},  # Вариант 1
    {"a1": 2, "a2": 4, "a3": 6, "n1": 10, "n2": 12, "n3": 14},  # Вариант 2
    {"a1": 1, "a2": 3, "a3": 5, "n1": 7, "n2": 9, "n3": 11},    # Вариант 3
    # Добавьте остальные варианты...
]