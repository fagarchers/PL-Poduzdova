import tkinter as tk
from tkinter import ttk, filedialog, messagebox
#калькулятор
def create_calculator(frame):
    tk.Label(frame, text='число 1:').grid(row=0, column=0, padx=2, pady=5)
    n1 = tk.Entry(frame)
    n1.grid(row=0, column=1, padx=2, pady=5)

    tk.Label(frame, text='число 2:').grid(row=0, column=4, padx=2, pady=5)
    n2 = tk.Entry(frame)
    n2.grid(row=0, column=5, padx=2, pady=5)

    operations = ['+', '-', '*', '/']
    selected = tk.StringVar(value=operations[0])
    ttk.Label(frame, text='операция:').grid(row=0, column=2, padx=2, pady=5)
    menu = ttk.OptionMenu(frame, selected, operations[0], *operations)
    menu.grid(row=0, column=3, padx=2, pady=5)

    def calculate():
        try:
            a = float(n1.get())
            b = float(n2.get())
            o = selected.get()

            if o == '+':
                result = a + b
            elif o == '-':
                result = a - b
            elif o == '*':
                result = a * b
            elif o == '/':
                if b == 0:
                    raise ZeroDivisionError
                result = a / b
            messagebox.showinfo('результат', result)
        except ValueError:
            messagebox.showerror('ошибка', 'введите корректные числа')
        except ZeroDivisionError:
            messagebox.showerror('ошибка', 'деление на ноль невозможно')

    calc_button = ttk.Button(frame, text='посчитать', command=calculate)
    calc_button.grid(row=1, column=0, columnspan=6, pady=10)
#чекбоксики
def create_checkboxes(frame):
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()

    ttk.Checkbutton(frame, text='первый', variable=var1).pack(anchor='w', pady=2)
    ttk.Checkbutton(frame, text='второй', variable=var2).pack(anchor='w', pady=2)
    ttk.Checkbutton(frame, text='третий', variable=var3).pack(anchor='w', pady=2)

    def show_message():
        if var1.get():
            messagebox.showinfo('выбор', 'вы выбрали первый вариант')
        elif var2.get():
            messagebox.showinfo('выбор', 'вы выбрали второй вариант')
        elif var3.get():
            messagebox.showinfo('выбор', 'вы выбрали третий вариант')
        else:
            messagebox.showinfo('выбор', 'ничего не выбрано')

    button = ttk.Button(frame, text='показать выбор', command=show_message)
    button.pack(pady=10)
#меню для загрузки файла
def create_text(frame, window):
    maj_menu = tk.Menu(window)
    window.config(menu=maj_menu)
    file_menu = tk.Menu(maj_menu, tearoff=0)
    maj_menu.add_cascade(label='файл', menu=file_menu)

    def load_file():
        filename = filedialog.askopenfilename(title='выберите файл', filetypes=[('текстовые файлы', '*.txt')])
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    text_content.delete(1.0, tk.END)
                    text_content.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror('ошибка', 'не удалось открыть файл', str(e))

    file_menu.add_command(label='загрузить файл', command=load_file)

    text_content = tk.Text(frame)
    text_content.pack(expand=1, fill='both')

window = tk.Tk()
window.title('Подуздова Юлия Викторовна')
window.geometry('500x250')  
#стилёчек
style = ttk.Style()
style.theme_create( 'MyStyle', parent='alt', settings={
    'TNotebook': {'configure': {'tabmargins': [4, 4, 4, 4]}},
    'TNotebook.Tab': {'configure': {'padding': [40, 5]}, }})
style.theme_use('MyStyle')
#вкладочки
notebook = ttk.Notebook(window)
notebook.pack(expand=1, fill='both', padx=10, pady=10)
v1 = tk.Frame(notebook)
notebook.add(v1,text='калькулятор')
create_calculator(v1)

v2 = tk.Frame(notebook)
notebook.add(v2, text='чекбоксы')
create_checkboxes(v2)

v3 = tk.Frame(notebook)
notebook.add(v3, text='работа с текстом')
create_text(v3, window)

window.mainloop()

