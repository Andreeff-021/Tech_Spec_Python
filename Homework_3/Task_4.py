# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things = {'карта': 1, 'платка': 11, 'компас': 3, 'нож': 4, 'консервы': 8, 'аптечка': 5}
backpack = 20
things_in_backpack = []

for key, value in things.items():
    backpack -= value
    if backpack >= 0:
        things_in_backpack.append(key)
print(things_in_backpack)