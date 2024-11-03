def element_sum(data):
    sum_ = 0

    for item in data:
        if isinstance(item, (int, float)): # элемент  число
            sum_ += item
        elif isinstance(item, str): # работа со строкой
            sum_ += len(item)
        elif isinstance(item, (list, tuple)): # работа со списком или кортежем
            sum_ += element_sum(item)
        elif isinstance(item, dict): # работа со словарем
            for key, value in item.items():
                sum_ += element_sum([key, value])

        elif isinstance(item, set): # работа с множеством
            sum_ += element_sum(list(item))  

    return sum_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = element_sum(data_structure)
print(result)

data_structure = [
    [5, 8, 7, 0, 3],
    {'a': 4, 'b': 5},
    (6, {'sphere': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 45))}])
]
result = element_sum(data_structure)
print(result)