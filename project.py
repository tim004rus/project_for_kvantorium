from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton


#Program name
window = Tk()
window.title("Название файлов")
window.geometry('250x250')


# MessageBox
def a():
	messagebox.askquestion('Доклад/сочинение', 'Название файла')
def a():
	messagebox.showinfo('Доклад/сочинение', 'Название файла')
def b():
	messagebox.showinfo('Творческая работа', 'Название файла')
def c():
	messagebox.showinfo('Каталог/сборник', 'Название файла')
def d():
	messagebox.showinfo('Другое', 'Название файла')


# Label
lbl = Label(window, text='Выберите категорию файла:')
lbl.grid(column=0, row=0)


#Radio Buttons
rad1 = Radiobutton(window, text="Доклад/сочинение", value=1, command=a)
rad1.grid(column=0, row=3)
rad2 = Radiobutton(window, text="Творческая работа", value=2, command=b)
rad2.grid(column=0, row=4)
rad3 = Radiobutton(window, text="Каталог/сборник", value=3, command=c)
rad3.grid(column=0, row=5)
rad4 = Radiobutton(window, text="Другое", value=4, command=d)
rad4.grid(column=0, row=6)


window.mainloop()

# def a():
# 	messagebox.askquestion('Доклад/сочинение', 'Название файла')
