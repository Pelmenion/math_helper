from tkinter import *
import math as m
from tkinter import messagebox
import webbrowser


# Функции
def comming_soon():
    messagebox.showinfo('Coming soon', 'Тут пока ничего нету ＞﹏＜')

def Git():
    webbrowser.open_new('https://github.com/Pelmenion/math_helper')


def algebra():
    algebra_page = Toplevel(home_page)
    algebra_page.title("Algrbra")
    algebra_page.geometry('200x110')
    algebra_page.resizable(FALSE, FALSE)

    def algebra1():
        w = Toplevel(algebra_page)
        w.geometry('300x250')
        w.title('Решатель уравнений')
        w.resizable(FALSE, FALSE)

        data_labelframe = LabelFrame(w, text='Введите исходные данные')
        data_labelframe.pack()

        label_text1 = Label(data_labelframe, text="x**2 +")
        label_text1.grid(column=1, row=0, padx=10, pady=10)

        label_text2 = Label(data_labelframe, text='x +')
        label_text2.grid(column=3, row=0, padx=10, pady=10)

        label_text3 = Label(data_labelframe, text='= 0')
        label_text3.grid(column=5, row=0, padx=10, pady=10)

        entry_a = Entry(data_labelframe, width=2)
        entry_a.grid(column=0, row=0, padx=10, pady=10)

        entry_b = Entry(data_labelframe, width=2)
        entry_b.grid(column=2, row=0, padx=10, pady=10)

        entry_c = Entry(data_labelframe, width=2)
        entry_c.grid(column=4, row=0, padx=10, pady=10)

        def decision():
            try:
                a = int(entry_a.get())
                b = int(entry_b.get())
                c = int(entry_c.get())

                D = b ** 2 - (4 * a) * c

                if D >= 0:
                    x1 = (-b + m.sqrt(D)) / 2 * a
                    x2 = (-b - m.sqrt(D)) / 2 * a

                    output.delete(0.0, END)
                    output.insert(0.0, f"Дискриминант равен {D} \nx1 = {x1} \nx2 = {x2}")
                else:
                    output.delete(0.0, END)
                    output.insert(0.0, f"Дискриминант равен {D} \nУравнение не имеет решений.")
            except:
                messagebox.showerror('Ошибка!', "Убедитесь, что ввели все числа!")

        label_frame = LabelFrame(w, text='Решение')
        label_frame.pack(padx=10, pady=10)

        output = Text(label_frame, height=5)
        output.pack(padx=10, pady=10)

        buttn = Button(w, text='Решить уравнение', command=decision)
        buttn.pack(padx=10, pady=10)

    def algebra2():
        alpebra2 = Toplevel(algebra_page)
        alpebra2.title("Root of a number")
        alpebra2.geometry('250x200')

        def root_of_num():
            try:
                num = int(entry_int.get())
                ans = m.sqrt(num)
                entry_answer.delete(0, END)
                entry_answer.insert(0, ans)
            except:
                messagebox.showerror("Ошибка!", "Убедитесь в правильности введенного числа!")


        label_frame_int1 = LabelFrame(alpebra2, text='Введите число')
        label_frame_int1.pack(padx=5, pady=5)

        entry_int = Entry(label_frame_int1, width=10)
        entry_int.pack(padx=5, pady=5)

        label_frame_answer = LabelFrame(alpebra2, text='Ответ')
        label_frame_answer.pack(padx=5, pady=5)

        entry_answer = Entry(label_frame_answer, width=20)
        entry_answer.pack(padx=5, pady=5)

        bttn_show_answer = Button(alpebra2, text='Вычислить', command=root_of_num)
        bttn_show_answer.pack(pady=10)

    label_frame_algebra = LabelFrame(algebra_page, text='Выберите')
    label_frame_algebra.pack(padx=5, pady=5)

    bttn_algebra1 = Button(label_frame_algebra, text='Квадратные уравнения', command=algebra1)
    bttn_algebra1.pack(padx=5, pady=5)

    bttn_algebra2 = Button(label_frame_algebra, text='Корень числа', command=algebra2)
    bttn_algebra2.pack(padx=5, pady=5)

def geometry():
    messagebox.showinfo('Coming soon', 'Тут пока ничего нету ＞﹏＜')




# Домашняя страница
home_page = Tk()
home_page.geometry('300x240')
home_page.resizable(FALSE, FALSE)
home_page.title('Math helper')

# Интерфейс
label_hello = Label(text="Добро пожаловать в \nМатематический помощник!")
label_hello.pack()

label_frame_choose = LabelFrame(home_page, text="Выберете предмет:")
label_frame_choose.pack(pady=10)

bttn_algebra = Button(label_frame_choose, text="Алгебра", command=algebra)
bttn_algebra.grid(row=0, column=0, padx=5, pady=5)

bttn_geometry = Button(label_frame_choose, text="Геометрия", command=geometry)
bttn_geometry.grid(row=0, column=1, padx=5, pady=5)

bttn_check_update = Button(home_page, text="Проверить обновления", command=comming_soon)
bttn_check_update.pack(padx=5, pady=5)

label_version = Label(text='Версия 0.0.1')
label_version.pack(side=BOTTOM)

bttn_git = Button(home_page, text='GitHub', command=Git)
bttn_git.pack(padx=5, pady=30)


home_page.mainloop()