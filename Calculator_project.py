import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        value1 = float(entry1.get())
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Invalid first number: {e}")
        return

    try:
        value2 = float(entry2.get())
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Invalid second number: {e}")
        return

    results = []

    # Addition
    try:
        add = value1 + value2
        results.append(f"Addition: {add}")
    except Exception as e:
        results.append(f"Addition Error: {e}")

    # Subtraction
    try:
        sub = value1 - value2
        results.append(f"Subtraction: {sub}")
    except Exception as e:
        results.append(f"Subtraction Error: {e}")

    # Multiplication
    try:
        mul = value1 * value2
        results.append(f"Multiplication: {mul}")
    except Exception as e:
        results.append(f"Multiplication Error: {e}")

    # Division
    try:
        div = value1 / value2
        results.append(f"Division: {div}")
    except Exception as e:
        results.append(f"Division Error: {e}")

    # Modulus
    try:
        mod = value1 % value2
        results.append(f"Modulus: {mod}")
    except Exception as e:
        results.append(f"Modulus Error: {e}")

    result_label.config(text="\n".join(results))


# Create GUI window
root = tk.Tk()
root.title("Robust Calculator")
root.geometry("400x400")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
