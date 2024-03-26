def delete():
    id_note = input("Введите номер заметки, которую хотите удалить: ")
    with open('text2.csv', 'r') as file:
        load = file.readlines()
        total_notes = {}
        for i in range(len(load)):
            new = load[i].split(";")
            id = new[0]
            time = new[1].strip()
            title = new[2].strip()
            text = new[3].strip()
            note = {id: {time: {title: text}}}
            total_notes.update(note)

        total_notes.pop(id_note, "Неверно ввели номер заметки.")

        with open('text2.csv', 'w') as file:
            for id, time_note in total_notes.items():
                for time, note in total_notes[id].items():
                    for title, text in total_notes[id][time].items():
                        file.write(f'{id}; {time}; {title}; {text}\n')
    print("Заметка удалена.\n")
    file.close()

