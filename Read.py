import datetime
def read():
    print("\nВыберите действие:\n"
          "Вывести заметки за определенный период времени - filter.\n"
          "Вывести все заметки - all.\n")
    com = input("Введите команду: ").upper()

    if com == "ALL":
        with open('text2.csv', 'r') as file:
            load = file.readlines()
        for i in range(1, len(load)):
            new = load[i].split(";")
            print(f'{new[0]}; {new[1].strip()}; {new[2].strip()}; {new[3].strip()}')
        file.close()
        print('\n')

    if com == "FILTER":
        flag = True
        while flag:
            try:
                day_start = int(input("День начала периода: "))
                month_start = int(input("Месяц начала периода: "))
                year_start = int(input("Год начала периода: "))
                day_finish = int(input("День окончания периода: "))
                month_finish = int(input("Месяц окончания периода: "))
                year_finish = int(input("Год окончания периода: "))
            except ValueError:
                print("Ошибка ввода числа.")
            if month_start > 12 or month_finish > 12:
                print("Ошибка ввода месяца. Повторите ввод заново.")
                break
            if (month_start == 2 and day_start > 29) or (day_start > 31):
                print("Ошибка ввода дня. Повторите ввод заново.")
                break

            try:
                data_start = f'{year_start}-{month_start}-{day_start}'
                data_finish = f'{year_finish}-{month_finish}-{day_finish}'
                data_s = datetime.datetime.strptime(data_start, '%Y-%m-%d')
                data_f = datetime.datetime.strptime(data_finish, '%Y-%m-%d')
            except (NameError, ValueError):
                print("Ошибка ввода числа тут.")
                raise ValueError

            with open('text2.csv', 'r') as file:
                load = file.readlines()
                total_notes = {}
                for i in range(1, len(load)):
                    new = load[i].split(";")
                    id_n = new[0]
                    time = new[1].strip()
                    title = new[2].strip()
                    text = new[3].strip()
                    note = {id_n: {time: {title: text}}}
                    total_notes.update(note)


                    time_n = datetime.datetime.strptime(time, '%Y-%m-%d')
                    if time_n.year >= year_start and time_n.year <= year_finish:
                        if time_n.month >= month_start and time_n.month <= month_finish:
                            if time_n.day >= day_start and time_n.day <= day_finish:
                                print(f'{id_n}; {time}; {title}; {text}')
            file.close()
            print('\n')
            flag = False
    if com != "ALL" and com != "FILTER":
        print("Не правильно введена команда.")