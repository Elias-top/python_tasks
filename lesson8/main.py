# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# Показывает всю информацию в файле
def show_data(filename):
	with open(filename, 'r', encoding='utf-8') as data:
		print(data.read())
		print('')

# Записывает информацию в файл
def add_data(filename):
	with open(filename, 'a', encoding='utf-8') as data:
		fio = input('Введите ФИО: ')
		phone_number = input('Введите номер телефона: ')
		data.write(f'{fio} | {phone_number}\n')
		print(f'Добавлена запись : {fio} | {phone_number}\n')

# Изменяет информацию из файла
def edit_data(filename):
	temp_index = 0
	temp_same_index_array = []
	with open(filename, 'r', encoding='utf-8') as data:
		tel_book = data.readlines()
		print(tel_book)
		print('')
		fio = input('Введите текущую фамилию, имя или телефон для редактирования: ')

		for index in range(len(tel_book)):
			if fio in tel_book[index]:
				temp_same_index_array.append(index)
				temp_index += 1
				print(f"По вашему запросу обнаружен человек: {temp_index}. {tel_book[index]}")
	
		if (len(temp_same_index_array) > 1):
			temp_index = int(input("По вашему запросу найдено больше чем один человек. Выберите индекс человека, данные которого изменить "))
			print(f"Для изменения выбран {tel_book[temp_same_index_array[temp_index - 1]]}")
		elif(len(temp_same_index_array) == 0):
			print("По вашему запросу ничего не найдено")
			return
		
		index_delete_data = temp_same_index_array[temp_index - 1]

		elements = tel_book[index_delete_data].split(' | ')
		fio = input('Введите ФИО: ')
		phone = input('Введите номер телефона: ')
		if len(fio) == 0:
			fio = elements[0]
		if len(phone) == 0:
			phone = elements[1]
		edited_line = f'{fio} | {phone} \n'
		print(f'Запись — {tel_book[index_delete_data][:-1]}, изменена на — {edited_line}\n')
		tel_book[index_delete_data] = edited_line
	with open(filename, 'w', encoding='utf-8') as f:
	 	f.write(''.join(tel_book))


# Удаляет информацию из файла
def delete_data(filename):
	temp_index = 0
	temp_same_index_array = []
	with open(filename, 'r', encoding='utf-8') as data:
		tel_book = data.readlines()
		print(tel_book)
		print('')
		fio = input('Введите текущую фамилию, имя или телефон для удаления: ')

		for index in range(len(tel_book)):
			if fio in tel_book[index]:
				temp_same_index_array.append(index)
				temp_index += 1
				print(f"По вашему запросу обнаружен человек: {temp_index}. {tel_book[index]}")
	
		if (len(temp_same_index_array) > 1):
			temp_index = int(input("По вашему запросу найдено больше чем один человек. Выберите индекс человека, данные которого удалить "))
			print(f"Для изменения выбран {tel_book[temp_same_index_array[temp_index - 1]]}")
		elif(len(temp_same_index_array) == 0):
			print("По вашему запросу ничего не найдено")
			return
		
		index_delete_data = temp_same_index_array[temp_index - 1]

		print(f'Запись — {tel_book[index_delete_data][:-1]} удалена\n')
		tel_book.pop(index_delete_data)
	with open(filename, 'w', encoding='utf-8') as f:
	 	f.write(''.join(tel_book))

def main():
	my_choice = 3
	file_tel = 'tel.txt'

	# Создает файл если его нет в папке
	with open(file_tel, 'a', encoding='utf-8') as file:
		file.write('')

	while (my_choice != 0):
		print('Выберите одно из действий:')
		print('1 — Вывести информацию на экран')
		print('2 — Произвести запись данных')
		print('3 — Произвести изменение данных')
		print('4 — Произвести удаление данных')
		print('0 — Выход из программы')
		action = int(input('Действие: '))
		if action == 1:
			show_data(file_tel)
		elif action == 2:
			add_data(file_tel)
		elif action == 3:
			edit_data(file_tel)
		elif action == 4:
			delete_data(file_tel)
		else:
			my_choice = 0

if __name__ == '__main__':
	main()