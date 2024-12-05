import tkinter as tk
from tkinter import ttk

def click(button_text):
    if button_text == "=":
        try:
            result = eval(enter.get())  # Выполняется расчет выражения - enter.get() считывает введённое
            # пользователем выражение в виде строки, Функция eval() интерпретирует строку как Python-код
            enter.delete(0, tk.END) # Очищается поле ввода с диапазоном 0: Указывает на начало строки (первая позиция
            # текста в поле Entry), tk.END: Указывает на конец строки (последний символ в поле).
            enter.insert(tk.END, str(result)) # Вставляется результат
        except Exception as e:
            enter.delete(0, tk.END)
            enter.insert(tk.END, "Exception: {e}") # Обработка ошибок, если выражение некорректно
    elif button_text == "C":
        enter.delete(0, tk.END)
    else:
        enter.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")

# Поле ввода
font_large = ("Arial", 20)  # Увеличенный шрифт
enter = tk.Entry(root, width=45, borderwidth=2, justify="right", font=font_large)
enter.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    (".", "0", "=", "+"),
    ("C",)
]

# Отображение кнопок в сетке - цикл проходит по каждому элементу в строке buttons и добавляет соответствующую кнопку на нужную позицию.
for r, row in enumerate(buttons, start=1):
    for c, button_text in enumerate(row):
        button = ttk.Button(
            root,
            text=button_text,
            command=lambda x=button_text: click(x),
            style="TButton",
            padding=(10, 10)  # Дополнительное выравнивание
        )
        button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5) # sticky="nsew" - кнопки должны растягиваться по
        # вертикали и горизонтали в своих ячейках.

# Настройка одинакового размера колонок и строк
for i in range(4):  # 4 колонки
    root.grid_columnconfigure(i, weight=1)
for i in range(len(buttons)):  # Количество строк равно количеству рядов кнопок
    root.grid_rowconfigure(i, weight=1)

# Создание стиля для кнопок
style = ttk.Style()
style.configure("TButton", font=font_large)

root.mainloop()




