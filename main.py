# # Напишіть функцію, що перевертає вміст списку цілих.
# def digit_reverse(lst: list):
#     return lst.reverse()
#
#
# new_lst = [1, 2, 3, 4, 5]
# digit_reverse(new_lst)

# Напишіть функцію, яка шукає деяке число у списку цілих.
# def search_number_in_list(number, number_list):
#     count = number_list.count(number)
#     if count > 0:
#         return f"Digit {number} was used {count} times"
#     else:
#         return f"Digit {number} didn't used in list"
#
#
# my_list = [2, 4, 6, 8, 10, 6, 6, 4]
# searched_number = 6
#
# result = search_number_in_list(searched_number, my_list)
# print(result)
# Напишіть функцію, що обчислює факторіал кожного елемента списку цілих. Функція повертає новий список, який містить отримані факторіали.
# def find_fact(lst: list) -> list:
#     new_lst = []
#     for i in lst:
#         fact = 1
#         for j in range(1, i + 1):
#             fact *= j
#             new_lst.append(fact)
#             return new_lst
#
#
# new_lst = [1, 2, 3, 4, 5,]
# print(find_fact(new_lst))
# Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
# def multiply_list_elements(number_list):
#     result = 1
#     for num in number_list:
#         result *= num
#     return result
#
#
# my_list = [2, 3, 4, 5]
# result = multiply_list_elements(my_list)
# print("Mult:", result)

# Напишіть функцію для знаходження мінімуму в списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
# def minimal_digit(lst: list) -> list:
#     lst = [1, 2, 3, 4, 5]
#     return min(lst)
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# result = minimal_digit(lst)
# print(f"Minimum:{result}")
# Напишіть функцію, що визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
# def defaultDigit():
#     lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     for i in range(len(lst)):
#         if i % 1 == i and i % i == 0:
#             lst.append(i)
#             return lst
#
#
# new_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = defaultDigit(new_lst)
# print(f"Default digits: {result}")

#За тією роботою, що ми писали на занятті, де діставали дані температури, виведіть на консоль швидкість вітру, країну та місто.
import requests

TOKEN = "bec0898504ab15a7dfc2d3fdceebe4f3"
TOKEN = "e8eea91bea749ae9ff445dbe30eb8d83"

url = "https://api.oneweathermap.org/data/2.5/weather/"
params = {"q": input("City ").title(), "appid": TOKEN}

data = requests.get(url, params=params)
print(data.status_code)

#Не понимаю почему не работает если я копирую у вас тот код, который вы мне кидали