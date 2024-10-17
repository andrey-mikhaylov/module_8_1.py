Summable = int | float | str


def add_everything_up(a: Summable, b: Summable) -> Summable:
    """
    принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух
    данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
    :param a: число(int, float) или строка(str).
    :param b: число(int, float) или строка(str).
    :return: сумма a и b
    """
    try:
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    return result


def test():
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
    """
    Вывод в консоль:
    123.456строка
    яблоко4215
    130.456
    """


if __name__ == '__main__':
    test()


"""
2023/11/24 00:00|Домашнее задание по теме "Try и Except"
Домашнее задание по уроку "Try и Except".

Задание "Программистам всё можно":
Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int) 
и строку(str)? Давайте исправим это недоразумение!

Реализуйте следующую функцию:
add_everything_up, будет складывать числа(int, float) и строки(str)

Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух 
данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.

Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

Вывод в консоль:
123.456строка
яблоко4215
130.456

Примечания:
Конструкции try-except в функции выполняют строго ту обработку, которая написана в задании 
(обращайте на важность порядка передачи данных).
Если хотите дополнить функции своими исключениями или написать отдельно дополнительно собственные функции 
- это не запрещено, мы не против, чтобы вы больше экспериментировали. Но в первую очередь выполните поставленную задачу.

Файл module_8_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.

"""