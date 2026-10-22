import tkinter as tk
from tkinter import messagebox

# Переменные для хранения первого числа и выбранной операции
first_number = None
current_operation = None


def add_digit(digit):
    """Добавляет цифру в поле ввода."""
    current = text_input.get()
    text_input.delete(0, tk.END)
    text_input.insert(0, current + str(digit))


def clear():
    """Очищает поле ввода и сбрасывает выбранную операцию."""
    global first_number, current_operation
    text_input.delete(0, tk.END)
    first_number = None
    current_operation = None


def choose_operation(operation):
    """Запоминает первое число и выбранную арифметическую операцию."""
    global first_number, current_operation
    try:
        first_number = float(text_input.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Сначала введите число.")
        return

    current_operation = operation
    text_input.delete(0, tk.END)


# Пять функций, назначенных арифметическим кнопкам
def multiply(a, b):
    """Умножение."""
    return a * b


def divide(a, b):
    """Деление."""
    if b == 0:
        raise ZeroDivisionError
    return a / b


def summ(a, b):
    """Сложение."""
    return a + b


def diff(a, b):
    """Вычитание."""
    return a - b


def result():
    """Выполняет выбранную операцию и показывает результат."""
    global first_number, current_operation

    if first_number is None or current_operation is None:
        messagebox.showerror("Ошибка", "Выберите операцию после ввода первого числа.")
        return

    try:
        second_number = float(text_input.get())
        answer = current_operation(first_number, second_number)

        # Показываем целые числа без .0
        if isinstance(answer, float) and answer.is_integer():
            answer = int(answer)

        text_input.delete(0, tk.END)
        text_input.insert(0, str(answer))

        first_number = None
        current_operation = None
    except ValueError:
        messagebox.showerror("Ошибка", "Введите второе число.")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "На ноль делить нельзя.")


# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("340x440")
root.resizable(False, False)
root.configure(bg="#202431")

# Поле для ввода чисел и вывода результата
text_input = tk.Entry(
    root,
    font=("Arial", 22),
    justify="right",
    bd=0,
    bg="#f4f6fb",
    fg="#151824"
)
text_input.grid(row=0, column=0, columnspan=4, padx=12, pady=16, ipady=12, sticky="nsew")

# Матрица кнопок: цифры и арифметические операции
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for label, row, column in buttons:
    if label.isdigit():
        command = lambda digit=label: add_digit(digit)
    elif label == "+":
        command = lambda: choose_operation(summ)
    elif label == "-":
        command = lambda: choose_operation(diff)
    elif label == "*":
        command = lambda: choose_operation(multiply)
    elif label == "/":
        command = lambda: choose_operation(divide)
    elif label == "=":
        command = result
    else:
        command = clear

    color = "#3c4560" if label.isdigit() else "#276b9a"
    if label == "=":
        color = "#24a36b"
    elif label == "C":
        color = "#b94b55"

    tk.Button(
        root,
        text=label,
        command=command,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="white",
        activebackground="#596887",
        activeforeground="white",
        bd=0,
        relief="flat"
    ).grid(row=row, column=column, padx=5, pady=5, ipadx=8, ipady=12, sticky="nsew")

for column in range(4):
    root.grid_columnconfigure(column, weight=1)
for row in range(1, 5):
    root.grid_rowconfigure(row, weight=1)

root.mainloop()