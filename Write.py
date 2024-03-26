import csv
import datetime

def write():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    current_date = datetime.date.today().isoformat()

    with open('text2.csv', 'r') as file:
        load = file.readlines()
        count_id = []
        for i in range(len(load)):
            new = load[i].split(";")
            count_id.append(new[0])
    file.close()

    with open('text2.csv', 'a') as file:
        file.write(f'{int(count_id[-1]) + 1}; {current_date}; {title}; {text}\n')
    print("Заметка добавлена и сохранена.\n")
    file.close()