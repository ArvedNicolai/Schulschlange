import tkinter as tk
from tkinter import messagebox
import random

class Vokabel:
    def __init__(self, wort_d, wort_e, gewusst=False):
        self.wort_d = wort_d
        self.wort_e = wort_e
        self.versuche = 0
        self.gewusst = gewusst


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


# Globale Variable für die Vokabel des Tages
vokabelDesTages = Vokabel("Haus", "house")  # Beispiel-Vokabel des Tages

class Vokabeltrainer(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.vokabeln = [None] * 20
        self.freier_index = 0
        self.aktuell = 0

        # Beispielvokabeln hinzufügen
        self.vokabeln[self.freier_index] = Vokabel("Tisch", "table")
        self.freier_index += 1
        self.vokabeln[self.freier_index] = Vokabel("Stuhl", "chair")
        self.freier_index += 1
        self.vokabeln[self.freier_index] = Vokabel("Tür", "door")
        self.freier_index += 1
        self.vokabeln[self.freier_index] = Vokabel("Apfel", "apple")
        self.freier_index += 1
        self.vokabeln[self.freier_index] = Vokabel("Eichhörnchen", "squirrel")
        self.freier_index += 1
        self.vokabeln[self.freier_index] = Vokabel("Informatik", "computer science")
        self.freier_index += 1
        # AUfgabe 2a[2]
        self.vokabeln[self.freier_index] = vokabelDesTages  # Vokabel des Tages auf Position 7 (Index 6)
        self.freier_index += 1
        # AUfgabe 2a[1]
        self.vokabeln[self.freier_index] = Vokabel("Löwe", "lion")
        self.freier_index += 1

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

        self.button_zeigen = tk.Button(self, text="Zeige ungewusstes deutsches Wort", command=self.b_zeige_deutsches_wort_ungewusst_action)
        self.button_zeigen.pack()

        self.button_pruefen = tk.Button(self, text="Prüfen", command=self.b_pruefen_action)
        self.button_pruefen.pack()

        self.button_hinzufuegen = tk.Button(self, text="Hinzufügen", command=self.b_hinzufuegen_action)
        self.button_hinzufuegen.pack()

        self.label_ausgabe = tk.Label(self, text="")
        self.label_ausgabe.pack()

        # Zeige die Vokabel des Tages bei Programmstart
        self.zeige_vokabel_des_tages()

# AUfgabe 2a[2]
    def zeige_vokabel_des_tages(self):
        """Zeigt die Vokabel des Tages in den Eingabefeldern an."""
        self.entry_deutsch.delete(0, tk.END)
        self.entry_deutsch.insert(0, vokabelDesTages.get_wort_d())
        self.entry_englisch.delete(0, tk.END)
        self.entry_englisch.insert(0, vokabelDesTages.get_wort_e())
        # Setze aktuell auf die Position der Vokabel des Tages in der Liste
        self.aktuell = 6

    def b_zeige_deutsches_wort_action(self):
        """Wählt zufällig eine Vokabel aus der Liste und zeigt sie an."""
        if self.freier_index > 1:  # Sicherstellen, dass mindestens eine Vokabel vorhanden ist
            self.aktuell = random.randint(0, self.freier_index - 1)
            self.entry_deutsch.delete(0, tk.END)
            self.entry_deutsch.insert(0, self.vokabeln[self.aktuell].get_wort_d())
            self.entry_englisch.delete(0, tk.END)

    def b_zeige_deutsches_wort_ungewusst_action(self):
        """Wählt eine Vokabel aus der Liste, die nicht gewusst wurde, und zeigt sie an."""

        ungewusste_vokabel = None
        for vokabel in self.vokabeln:
        #Vokabeln durchlaufen, damit bei jedem Wort getestet wird, ob die Vokabel gewusst wurde. 
            if not vokabel.gewusst:
                ungewusste_vokabel = vokabel
                break
        
        if ungewusste_vokabel: 
            #selbe Anweisung, wie bei zeige_deutsches_wort
            self.entry_deutsch.delete(0, tk.END)
            self.entry_deutsch.insert(0, ungewusste_vokabel.wortD)
            self.entry_englisch.delete(0, tk.END)
            self.aktuell = self.vokabeln.index(ungewusste_vokabel)
        else:
            #nur dann wenn es keine ungewussten Vokabeln mehr gibt
            self.label_ausgabe.config(text="Alle Vokabeln wurden bereits richtig eingegeben!")


    def b_pruefen_action(self):
        wd = self.entry_deutsch.get()
        we = self.entry_englisch.get()
        if self.vokabeln[self.aktuell].pruefen(wd, we):
            self.label_ausgabe.config(text="Das war richtig, super")
        else:
            self.label_ausgabe.config(text="Leider falsch")

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
