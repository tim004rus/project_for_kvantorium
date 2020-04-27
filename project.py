from tkinter import *
from tkinter.ttk import Radiobutton


#Program name
window = Tk()
window.title("Название файлов")
window.geometry('400x250')


# Label
lbl = Label(window, text='Выберите категорию файла:')
lbl.grid(column=0, row=0)


#Radio Buttons
rad1 = Radiobutton(window, text="Доклад/сочинение", value=1)
rad1.grid(column=0, row=3)
rad2 = Radiobutton(window, text="Творческая работа", value=2)
rad2.grid(column=0, row=4)
rad3 = Radiobutton(window, text="Каталог/сборник", value=3)
rad3.grid(column=0, row=5)
rad4 = Radiobutton(window, text="Другое", value=4)
rad4.grid(column=0, row=6)

window.mainloop()
