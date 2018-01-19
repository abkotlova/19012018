# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def full_list():
	migrations_dir = os.path.join(current_dir, migrations)
	first_list = os.listdir(path=migrations_dir)
	return first_list


def search_sql(full_list):
	sql_list = list()
	for i in full_list:
		if i.endswith(".sql"):
			sql_list.append(i)
	return sql_list


def read_file(file_name):
	with open(os.path.join(current_dir, migrations, file_name), "r") as f:
    data = f.read()


def search_line(search_sql):
	first_list = search_sql
	while True:
		search = input("Введите строку:")
		new_list = list()
		for file_name in list:
			if search in read_file(file_name):
				new_list.append(file_name)
				print(file_name)
		print ("Всего: {}".format(len(new_list)))	
		first_list = new_list	


if __name__ == '__main__':
    search_line(search_sql(full_list()))
    pass