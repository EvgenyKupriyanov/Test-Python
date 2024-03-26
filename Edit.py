import datetime

def edit():
	id_note = input("Введите номер заметки, которую хотите изменить: ")
	with open('text2.csv', 'r') as file:
		load = file.readlines()
		total_notes = {}
		for i in range(len(load)):
			new = load[i].split(";")
			id_n = new[0]
			time = new[1].strip()
			title = new[2].strip()
			text = new[3].strip()
			note = {id_n: {time: {title: text}}}
			total_notes.update(note)
		old_time = list(total_notes[id_note].keys())
		old_title = list(total_notes[id_note].values())
		old_title2 = list(old_title[0].keys())
		old_text = list(old_title[0].values())
		old_note = f'{id_note}; {old_time[0]}; {old_title2[0]}; {old_text[0]}\n'

		title = input("Введите новый заголовок заметки: ")
		text = input("Введите новый текст заметки: ")
		current_date = datetime.date.today().isoformat()
		note_edit = f'{id_note}; {current_date}; {title}; {text}\n'

		with open('text2.csv', 'r') as file:
			file_data = file.read()
			file_data = file_data.replace(old_note, note_edit)
			with open('text2.csv', 'w') as file:
				file.write(file_data)
	print("Заметка изменена и сохранена.\n")
	file.close()











	# with open('text2.csv', 'r') as file:
	# 	file_data = file.read()
	# 	title = input("Введите новый заголовок заметки: ")
	# 	text = input("Введите новый текст заметки: ")
	# 	current_date = datetime.date.today().isoformat()
	# 	note_edit = {id_note: {current_date: {title: text}}}
	# 	file_data = file_data.replace(old, note_edit)
	# 	with open('text2.csv', 'w') as file:
	# 		file.write(file_data)
	#
	#
	#
    # for id, time_note in newN.items():
 	#     for time, note in  newN[id].items():
 	# 	    for title, text in newN[id][time].items():
 	# 		    newNN = f'{id}; {time}; {title}; {", ".join(text)}\n'
	#
	#
	#
	#
    # with open('text2.csv', 'w') as file:
	#     file.write(file_data)
	#
    # with open('text2.csv', 'a') as file:
	#     for id, time_note in newN.items():
	# 	    for time, note in  newN[id].items():
	# 		    for title, text in newN[id][time].items():
	# 			    file.write(f'{id}; {time}; {title}; {", ".join(text)}\n')