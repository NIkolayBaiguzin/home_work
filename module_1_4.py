#Практическая работа по уроку "Организация программ и методы строк." 04/10/2024

my_string = input("Напишите о себе:")
user_text_len = len(my_string.strip()) # strip() Удаление пробельных символов в начале и в конце строки.

print(f'В тексте ведёном пользователем {user_text_len} символов!' )

print(my_string.upper()) # Вывод текста в верхнем регистре.
print(my_string.lower()) # Вывод текста в нижнем регистре.
print(my_string.replace(' ', '')) # Заменяем пробелы на пустоту или удаляем каму как удобно.
print(my_string.strip()[0]) # Выводит первый символ! Удалил пробелы если пользователь случайно поставил.
print(my_string.strip()[-1])# Выводит последний символ! Удалил пробелы если пользователь случайно поставил.
