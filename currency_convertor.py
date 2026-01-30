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
root.geometry("450x350")
root.resizable(False, False)

BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
ENTRY_BG = "#2d2d2d"
ACCENT = "#3a7ff6"

root.configure(bg=BG_COLOR)

tk.Label(
    root,
    text="Amount",
    bg=BG_COLOR,
    fg=FG_COLOR,
    font=("Segoe UI", 11)
).pack(pady=(10, 2))

amount_entry = tk.Entry(
    root,
    bg=ENTRY_BG,
    fg=FG_COLOR,
    insertbackground=FG_COLOR,
    font=("Segoe UI", 11),
    relief="flat"
)
amount_entry.pack(ipadx=8, ipady=5)

tk.Label(
    root,
    text="From Currency (e.g. USD)",
    bg=BG_COLOR,
    fg=FG_COLOR,
    font=("Segoe UI", 11)
).pack(pady=(10, 2))

from_entry = tk.Entry(
    root,
    bg=ENTRY_BG,
    fg=FG_COLOR,
    insertbackground=FG_COLOR,
    font=("Segoe UI", 11),
    relief="flat"
)
from_entry.pack(ipadx=8, ipady=5)

tk.Label(
    root,
    text="To Currency (e.g. EUR)",
    bg=BG_COLOR,
    fg=FG_COLOR,
    font=("Segoe UI", 11)
).pack(pady=(10, 2))

to_entry = tk.Entry(
    root,
    bg=ENTRY_BG,
    fg=FG_COLOR,
    insertbackground=FG_COLOR,
    font=("Segoe UI", 11),
    relief="flat"
)
to_entry.pack(ipadx=8, ipady=5)

# --- Button ---
tk.Button(
    root,
    text="Convert",
    command=on_convert,
    bg=ACCENT,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    activebackground="#2f6bdc",
    activeforeground="white",
    cursor="hand2"
).pack(pady=15, ipadx=10, ipady=5)

# --- Result ---
result_label = tk.Label(
    root,
    text="",
    bg=BG_COLOR,
    fg=FG_COLOR,
    font=("Segoe UI", 15, "bold")
)
result_label.pack()

root.mainloop()