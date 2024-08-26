data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(*data):
    Summa = 0
    for i in data:
        if isinstance(i, int):
            Summa += i
        elif isinstance(i, str):
            Summa += len(i)
        elif isinstance(i, dict):
            Summa += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, tuple, set)):
            Summa += calculate_structure_sum(*i)
    return Summa


result = calculate_structure_sum(data_structure)
print(result)
