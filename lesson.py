# Объявляем функции и аргументы

# def print_func(open_browser, browser_name):
#     pass
#
#
# def open_browser(browser_name):
#    print_func(open_browser, browser_name)
# print(open_browser)

# def func():
#     print("я вызвалась!")
#
# func()

# Возвращаем значение


# def func_with_return():
#     return "я вернулся!"
#
#
# a = func_with_return()
# print(a)


# def func_with_arg(name="vasya", surname="some"):
#     print(f"я {name}!")


# func_with_arg()
# func_with_arg("masha")
# # func_with_arg(name="petya")

# Переменное количество аргументов

#
# def custom_print(*args):
#     print(*args, sep=", ")
#
# custom_print(2, 'wer', 99)

# def another_print(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)


# custom_print(1, 2, 3)
#
# another_print(key="value", first="second")

# Переменное количество возвращаемых значений

# Функция - тоже объект

# p = print
# p("hello, world!")

#
# def by_age(d):
#     return d["age"]
#
#
# by_age({"name": "Oleg", "age": 32})
#
#
# users = [
#     {"name": "Oleg", "age": 32},
#     {"name": "Sergey", "age": 24},
#     {"name": "Stanislav", "age": 15},
#     {"name": "Olga", "age": 45},
#     {"name": "Maria", "age": 18},
# ]
#
# print(sorted(users, key=by_age))


num = int(input())

while num != 0:
    last_digit = num % 10

    num = num // 10
    print(last_digit)