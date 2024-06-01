import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    results = {
        "length": False,
        "uppercase": False,
        "number": False,
        "spaces": True
    }

    if 8 <= len(password) <= 20:
        results["length"] = True

    if re.search(r'[A-Z]', password):
        results["uppercase"] = True

    if re.search(r'\d', password):
        results["number"] = True

    if not re.search(r'\s', password):
        results["spaces"] = True

    return results

def evaluate_strength(results):
    if all(results.values()):
        return "Strong"
    elif results["length"] and (results["uppercase"] or results["number"]):
        return "Medium"
    else:
        return "Weak"

def display_results(results):
    result_str = "Password must include:\n"
    result_str += f"8-20 Characters: {'✓' if results['length'] else '✗'}\n"
    result_str += f"At least one capital letter: {'✓' if results['uppercase'] else '✗'}\n"
    result_str += f"At least one number: {'✓' if results['number'] else '✗'}\n"
    result_str += f"No spaces: {'✓' if results['spaces'] else '✗'}\n"
    return result_str

def check_password():
    password = entry.get()
    results = check_password_strength(password)
    result_str = display_results(results)
    strength = evaluate_strength(results)
    messagebox.showinfo("Password Strength", f"{result_str}\nPassword Strength: {strength}")

app = tk.Tk()
app.title("Password Complexity Checker By Virupakshi")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter your password:")
label.pack(pady=5)

entry = tk.Entry(frame, show='*', width=30)
entry.pack(pady=5)

show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=lambda: entry.config(show='' if show_password_var.get() else '*'))
show_password_check.pack(pady=5)

check_button = tk.Button(frame, text="Check Password", command=check_password)
check_button.pack(pady=10)

app.mainloop()
