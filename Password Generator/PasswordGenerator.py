import uuid
import random
from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Password Generator")

heading = Label(root, width=30, justify=CENTER, fg='red', text="Password : ",font=('Times', 20, "bold"))  
heading.pack(pady=(50, 0))  

pass_variable = StringVar()

text_input = Entry(root, width=30, justify=CENTER, textvariable=pass_variable, font=('Times', 20,'bold'))
# my_text.pack(padx=50, pady=150)
text_input.pack(pady=(50, 0))


def password_generator():
	password_length = 6
	possible_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*+?><.:;'

	password = ''

	for i in range(password_length):
		password = password + random.choice(possible_char)

	uuid_result = uuid.uuid1()
	# get the first 6 char from uuid_result
	shortened_uuid = str(uuid_result)[:6]

	password = password + shortened_uuid
	pass_variable.set(password)


button = Button(root, justify=CENTER, fg='red', text='Generate Password', font=(10), command=password_generator)
button.pack(pady=(30, 0))
button.pack()

while True:
	root.mainloop()