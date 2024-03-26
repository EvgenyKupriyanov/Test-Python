import csv
import pickle
import datetime
from Write import write
from Read import read
from Start import start
from Delete import delete
from Edit import edit




start()
while (True):
	selection = input("1.Добавить заметку - add\n"
					  "2.Чтение заметки - read\n"
					  "3.Изменить заметку - edit\n"
					  "4.Удалить заметку - delete\n"
					  "5.Выход - exit\n"
					  "Выберите действие: ").upper()
	match selection:
		case "ADD":
			write()
		case "READ":
			read()
		case "EDIT":
			edit()
		case "DELETE":
			delete()
		case "EXIT":
			break
		case _:
			print("Некорректный ввод")

print("Программа завершена")


