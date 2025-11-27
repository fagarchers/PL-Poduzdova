import tkinter as tk
from tkinter import messagebox
import json
import requests
def getting_repository_data():
    repository = entry.get()
    if not repository:
        messagebox.showerror('ошибка')
        return

    url = f'https://api.github.com/repos/{repository}'
    try:
        answer = requests.get(url)
        answer.raise_for_status()
        data = answer.json()
        finding = {'company': data.get('company'), 'created_at': data.get('created_at'), 'email': data.get('email'), 'id': data.get('id'), 'name': data.get('name'), 'url': data.get('html_url')}
                   
        with open('repository_data.json', 'w') as file:
                   json.dump(finding, file)
        messagebox.showinfo('данные успешно сохранены в файл')
    except requests.exceptions.RequestException as e:
        messagebox.showerror('ошибка')
    except json.JSONDecodeError:
        messagebox.showerror('ошибка')

window = tk.Tk()
window.title('Github information')
tk.Label(window, text='введите название репозитория:').pack()
entry = tk.Entry(window, width=50)
entry.pack()
button = tk.Button(window, text='получить данные', command=getting_repository_data)
button.pack()
window.mainloop()

                   
                   
                   
        
    
