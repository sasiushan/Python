import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.title("Reminders")


taskList = []
color = {}

def add_a_task():
	task = entry.get()
	if not task:
		print("It is empty")
	else:
		taskList.append(task)

	# clear the entry feild
		entry.delete(0, "end")
		update_taskList()

def remove_task():
	selected_task = display_list.curselection()

	if not selected_task:
		return

	position = selected_task[0]
	taskList.pop(position)

	display_list.selection_clear(position)

	update_taskList()


def update_taskList():
	# have to clear the list or else the tasks repeat
	display_list.delete(0, "end")

	count = 0
	for x in taskList:
		count += 1
		# f is basically used to format something into a string
		# {} is used to put an integer var.
		# checkbutton = tk.Checkbutton(display_list, text=x)
		# display_list.itemconfig(count, background='green')
		display_list.insert("end", f" {count}. {x}")



def completed_task():
	selected_task = display_list.curselection()

	if not selected_task:
		return

	position = selected_task[0]
	display_list.itemconfig(position, background='green')
	# color[position]= "green"
	display_list.selection_clear(0, "end")


word = tk.Label(window, text="Enter a task: ", font=('Lato', 20, "normal"))
word.pack(pady=(50, 0))

entry = tk.Entry(window)
entry.pack(pady=(10, 0))

add_button = tk.Button(window, text="Add", command=add_a_task)
add_button.pack(pady=(10, 0))

display_list = tk.Listbox(window)
# display_list.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)
display_list.config(width = 50)
display_list.pack(pady=(10, 0))

remove_button = tk.Button(window, text="Remove", fg='red', command=remove_task)
remove_button.pack(padx=100, side="left")

completed_button = tk.Button(window, text="Mark completed", command=completed_task)
completed_button.pack(side='left')

# cb = tk.Checkbutton(window)
# cb.pack()


window.mainloop()

