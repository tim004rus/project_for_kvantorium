# from & import
import random
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton


#Program name
window = Tk()
window.title("Названия для файлов")
window.geometry('300x300')

# Label
lbl = Label(window, text='Выберите категорию файла:')
lbl.grid(column=0, row=0)


# MessageBox
def rad1():
	window = Tk()
	window.title("Доклад/сочинение")
	window.geometry('400x80')

	def clicked():
		probability = random.randint(1, 4)

		if probability == 1:
			res = "Доклад про {}. Теперь и с перцем.".format(txt.get())
			lbl.configure(text=res)
		if probability == 2:
			res = "Сочинение о {}. Возможна поломка мозгов.".format(txt.get())
			lbl.configure(text=res)
		if probability ==3:
			res = "Доклад о {}. Не открывать до 30.07.30.".format(txt.get())
			lbl.configure(text=res)
		if probability == 4:
			res = "Сочинение о {}. Все права защищены.".format(txt.get())
			lbl.configure(text=res)


	lbl = Label(window, text='Введите общую тему в предложном падеже')
	lbl.grid(column=0, row=0)

	txt = Entry(window, width=20)
	txt.grid(column=0, row=1)

	btn = Button(window, text="Клик!", command=clicked)
	btn.grid(column=0, row=2)

	window.mainloop()


def rad2():
	window = Tk()
	window.title("Творческая работа")
	window.geometry('400x80')

	def clicked():
		probability = random.randint(1, 4)
		
		if probability == 1:
			res = "Творческая работа по теме {}. Кто нашёл тот здохнет".format(txt.get())
			lbl.configure(text=res)
		if probability == 2:
			res = "Творческая работа по теме {}. С любовью из психушки.".format(txt.get())
			lbl.configure(text=res)
		if probability ==3:
			res = "Творческая работа по теме {}. Дальтоникам посвящается...".format(txt.get())
			lbl.configure(text=res)
		if probability == 4:
			res = "Творческая работа по теме {}. Потом сделаю, честно".format(txt.get())
			lbl.configure(text=res)

	lbl = Label(window, text='Введите общую тему в предложном падеже')
	lbl.grid(column=0, row=0)

	txt = Entry(window, width=20)
	txt.grid(column=0, row=1)

	btn = Button(window, text="Клик!", command=clicked)
	btn.grid(column=0, row=2)

	window.mainloop()


def rad3():
	window = Tk()
	window.title("Каталог/сборник")
	window.geometry('400x80')

	def clicked():
		probability = random.randint(1, 4)
		
		if probability == 1:
			res = "Каталог {}. Он точно был где-то тут.".format(txt.get())
			lbl.configure(text=res)
		if probability == 2:
			res = "Сборник {}. Мы проверили, всё чисто.".format(txt.get())
			lbl.configure(text=res)
		if probability ==3:
			res = "Каталог {}. Кажется, вирусняк.".format(txt.get())
			lbl.configure(text=res)
		if probability == 4:
			res = "Сборник {}. Абсолютно бесполезен.".format(txt.get())
			lbl.configure(text=res)

	lbl = Label(window, text='Введите общую тему в предложном падеже')
	lbl.grid(column=0, row=0)

	txt = Entry(window, width=20)
	txt.grid(column=0, row=1)

	btn = Button(window, text="Клик!", command=clicked)
	btn.grid(column=0, row=2)

	window.mainloop()


def rad4():
	window = Tk()
	window.title("Другое")
	window.geometry('400x80')

	def clicked():
		probability = random.randint(1, 4)
		
		if probability == 1:
			res = "{}. Вход в даркнет рядом.".format(txt.get())
			lbl.configure(text=res)
		if probability == 2:
			res = "{}. Занято!".format(txt.get())
			lbl.configure(text=res)
		if probability ==3:
			res = "{}. Опять заразу из интернета тащит.".format(txt.get())
			lbl.configure(text=res)
		if probability == 4:
			res = "{}. Это не я, клянусь.".format(txt.get())
			lbl.configure(text=res)

	lbl = Label(window, text='Введите общую тему в родительном падеже')
	lbl.grid(column=0, row=0)

	txt = Entry(window, width=20)
	txt.grid(column=0, row=1)

	btn = Button(window, text="Клик!", command=clicked)
	btn.grid(column=0, row=2)

	window.mainloop()


#Radio Buttons
rad1 = Radiobutton(window, text="Доклад/сочинение", value=1, command=rad1)
rad2 = Radiobutton(window, text="Творческая работа", value=2, command=rad2)
rad3 = Radiobutton(window, text="Каталог/сборник", value=3, command=rad3)
rad4 = Radiobutton(window, text="Другое", value=4, command=rad4)
rad1.grid(column=0, row=3)
rad2.grid(column=0, row=4)
rad3.grid(column=0, row=5)
rad4.grid(column=0, row=6)


window.mainloop()
