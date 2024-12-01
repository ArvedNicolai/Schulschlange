import tkinter as tk
from tkinter import messagebox
import random
class Vokabel:
    def __init__(self, wort_d, wort_e):
        self.wort_d = wort_d
        self.wort_e = wort_e
        self.versuche = 0
        self.gewusst = False

    def reset(self):
        self.versuche = 0
        self.gewusst = False

    def pruefen(self, d, e):
        self.versuche += 1
        if self.wort_d == d and self.wort_e == e:
            self.gewusst = True
            return True
        else:
            self.gewusst = False
            return False

    def get_wort_d(self):
        return self.wort_d

    def set_wort_d(self, wort_d_neu):
        self.wort_d = wort_d_neu

    def get_wort_e(self):
        return self.wort_e

    def set_wort_e(self, wort_e_neu):
        self.wort_e = wort_e_neu

    def get_versuche(self):
        return self.versuche

    def get_gewusst(self):
        return self.gewusst

tagesvokabel = Vokabel("Armbanduhr", "watch")

class Vokabeltrainer(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.vokabeln = [None] * 20
        self.freier_index = 0
        self.aktuell = 0
        # Beispielvokabeln hinzufügen
        self.vokabeln[0] = Vokabel("Tisch", "table")
        self.vokabeln[1] = Vokabel("Stuhl", "chair")
        self.vokabeln[2] = Vokabel("Tür", "door")
        self.vokabeln[3] = Vokabel("Apfel", "apple")
        self.vokabeln[4] = Vokabel("Eichhörnchen", "squirrel")
        self.vokabeln[5] = Vokabel("Informatik", "computer science")
        self.vokabeln[6] = Vokabel("Löwe", "lion")
        self.vokabeln[7] = tagesvokabel
        self.freier_index = 8
        self.nichterstevokabel = 0
        # GUI erstellen
        self.title("Vokabeltrainer")
        self.geometry("400x200")

        self.label_deutsch = tk.Label(self, text="Deutsch:")
        self.label_deutsch.pack()

        self.entry_deutsch = tk.Entry(self)
        self.entry_deutsch.pack()

        self.label_englisch = tk.Label(self, text="Englisch:")
        self.label_englisch.pack()

        self.entry_englisch = tk.Entry(self)
        self.entry_englisch.pack()

        self.button_zeigen = tk.Button(self, text="Zeige deutsches Wort", command=self.b_zeige_deutsches_wort_action)
        self.button_zeigen.pack()
        self.button_zeigen = tk.Button(self, text="Zeige englisches Wort", command=self.b_zeige_englisches_wort_action)
        self.button_zeigen.pack()

        self.button_zeigen = tk.Button(self, text="reset", command=self.b_zeige_englisches_wort_action)
        self.button_zeigen.pack()
        
        self.button_pruefen = tk.Button(self, text="Prüfen", command=self.b_pruefen_action)
        self.button_pruefen.pack()

        self.button_hinzufuegen = tk.Button(self, text="Hinzufügen", command=self.b_hinzufuegen_action)
        self.button_hinzufuegen.pack()

        self.label_ausgabe = tk.Label(self, text="")
        self.label_ausgabe.pack()
    def b_zeige_deutsches_wort_action(self):
        self.aktuell = 7
        self.entry_deutsch.delete(0, tk.END)
        self.entry_deutsch.insert(0, tagesvokabel.get_wort_d())
        self.entry_englisch.delete(0, tk.END)
        
        if self.nichterstevokabel:
            self.aktuell = random.randint(0, self.freier_index - 1)
            while self.vokabeln[self.aktuell].gewusst !=  False:
                self.aktuell = random.randint(0, self.freier_index - 1)
            self.entry_deutsch.delete(0, tk.END)
            self.entry_deutsch.insert(0, self.vokabeln[self.aktuell].get_wort_d())
            self.entry_englisch.delete(0, tk.END)
        self.nichterstevokabel = True
        
    def b_zeige_englisches_wort_action(self):
        self.aktuell = 7
        self.entry_englisch.delete(0, tk.END)
        self.entry_englisch.insert(0, tagesvokabel.get_wort_e())
        self.entry_deutsch.delete(0, tk.END)
        
        if self.nichterstevokabel:
            self.aktuell = random.randint(0, self.freier_index - 1)
            while self.vokabeln[self.aktuell].gewusst !=  False:
                self.aktuell = random.randint(0, self.freier_index - 1)
            self.entry_englisch.delete(0, tk.END)
            self.entry_englisch.insert(0, self.vokabeln[self.aktuell].get_wort_e())
            self.entry_deutsch.delete(0, tk.END)
        self.nichterstevokabel = True

    def b_pruefen_action(self):
        wd = self.entry_deutsch.get()
        we = self.entry_englisch.get()
        richtig = self.vokabeln[self.aktuell].pruefen(wd, we)
        if richtig:
            self.label_ausgabe.config(text="Das war richtig, super, "  + "Versuche: " + str(self.vokabeln[self.aktuell].versuche))
        else:
            self.label_ausgabe.config(text="Leider falsch, " + "Versuche: " + str(self.vokabeln[self.aktuell].versuche))

    def b_hinzufuegen_action(self):
        if self.freier_index < len(self.vokabeln):
            wd = self.entry_deutsch.get()
            we = self.entry_englisch.get()
            self.vokabeln[self.freier_index] = Vokabel(wd, we)
            self.freier_index += 1
        else:
            messagebox.showinfo("Hinweis", "Die Liste ist voll!")

if __name__ == "__main__":
    app = Vokabeltrainer()
    app.mainloop()