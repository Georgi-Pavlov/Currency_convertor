import tkinter as tk
from tkinter import messagebox
from currency_functions import convert_currency


def on_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_entry.get()
        to_curr = to_entry.get()

        result = convert_currency(amount, from_curr, to_curr)

        if result is None:
            messagebox.showerror("Error", "Unsupported currency or API error!")
        else:
            result_label.config(
                text=f"{amount} {from_curr.upper()} = {result:.2f} {to_curr.upper()}"
            )

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for amount.")


root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x250")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="From Currency (e.g. USD)").pack()
from_entry = tk.Entry(root)
from_entry.pack()

tk.Label(root, text="To Currency (e.g. EUR)").pack()
to_entry = tk.Entry(root)
to_entry.pack()

tk.Button(root, text="Convert", command=on_convert).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()