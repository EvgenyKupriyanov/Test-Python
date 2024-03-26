def start():
    notes = {0: {'time': {'title': 'text'}}}
    with open('text2.csv', 'r') as file:
        load = file.readlines()
        if not load:
            with open('text2.csv', 'w') as file:
                for id, time_note in notes.items():
                    for time, note in notes[id].items():
                        for title, text in notes[id][time].items():
                            file.write(f'{id}; {time}; {title}; {text}\n')
    file.close()