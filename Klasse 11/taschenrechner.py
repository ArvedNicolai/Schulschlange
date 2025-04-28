import tkinter as tk
from tkinter import messagebox

def berechne():
    try:
        ausdruck = eingabe.get()
        ergebnis = eval(ausdruck)
        ausgabe.config(text="Ergebnis: " + str(ergebnis))
    except:
        messagebox.showerror("Fehler", "Ungültige Eingabe!")

# Fenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefeld
eingabe = tk.Entry(root, width=30)
eingabe.grid(row=0, column=0, columnspan=4)

# Ergebnisanzeige
ausgabe = tk.Label(root, text="Ergebnis: ")
ausgabe.grid(row=1, column=0, columnspan=4)

# Buttons für Zahlen & Operatoren
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, command=berechne, width=10)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: eingabe.insert(tk.END, t), width=10)
    button.grid(row=row, column=col)

# Hauptloop starten
root.mainloop()