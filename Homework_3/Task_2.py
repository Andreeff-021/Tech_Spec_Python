# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

some_list = [1, 3, 1, 3, 6, 7, 8, 5, 8]
list_duble_element = list(set(filter(lambda x: some_list.count(x) > 1, some_list)))
print(list_duble_element)
