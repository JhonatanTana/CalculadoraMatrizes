import tkinter as tk
from tkinter import messagebox


def calculate_determinant():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        d = int(entry_d.get())

        operarion = operation_var.get()

        if operarion == "Determinante":
            result = (a * d) - (b * c)
        elif operarion == "Adição":
            result = a + b + c + d
        elif operarion == "Subtração":
            result = a - b - c - d
        elif operarion == "Multiplicação":
            result = a * b * c * d
        else:
            result = "invalid operation"

        messagebox.showinfo("Resultado", f"Result {result}")

    except ValueError:
        messagebox.showerror("Erro", "invalid output")

root = tk.Tk()
root.title("matrix calculator")


root=tk.Tk()
root.title("Calculadora de Matriz Determinante")

Label_a = tk.Label(root, text="valor a:", bg='black', fg='white', font='blue')
Label_a.grid(row=0, column=0, sticky="w")
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

Label_b = tk.Label(root, text="valor b: ", bg='black', fg='white', font='blue')
Label_b.grid(row=1, column=0, sticky="w")
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

Label_c = tk.Label(root, text="valor c: ", bg='black', fg='white', font='blue')
Label_c.grid(row=2, column=0, sticky="w")
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

Label_d = tk.Label(root, text="valor d:", bg='black', fg='white', font='blue')
Label_d.grid(row=3, column=0, sticky="w")
entry_d = tk.Entry(root)
entry_d.grid(row=3, column=1)

operation_var = tk.StringVar()
operation_var.set("determinant")
operation_label = tk.Label(root, text="Select Operation: ", bg='black', fg='white', font='blue')
operation_label.grid(row=4, column=0, sticky="w")
operation_menu = tk.OptionMenu(root, operation_var, "Determinant", "Addition", "Subtraction", "Multiplication")
operation_menu.grid(row=4, column=1, sticky="w")

calculate_button = tk.Button(root, text="Calcular Determinante", command=calculate_determinant)
calculate_button.grid(row=5, columnspan=2, sticky="w")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()