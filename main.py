from random import choice

# 1. Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda f, s: f == s, first, second))
print(result)
# Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# 2. Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")  # Записываем каждое значение с новой строки
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3. Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())
