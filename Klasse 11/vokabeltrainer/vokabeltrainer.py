import csv
import os
import random
#Das sys-Modul enthält Funktionen und Variablen, die mit dem Python-Interpreter und der Systemumgebung arbeiten.
import sys  # Für sys.exit(), um das Programm jederzeit zu beenden

# Name der CSV-Datei
CSV_DATEI = "vokabeln.csv"

# Automatische Erstellung der CSV-Datei, falls sie nicht existiert
def erstelle_csv_datei():
    if not os.path.exists(CSV_DATEI):
        with open(CSV_DATEI, mode="w", newline="", encoding="latin-1") as file:
            writer = csv.writer(file)
            writer.writerow(["Deutsch", "Fremdsprache"])  # Kopfzeile hinzufügen
        print(f"📄 Datei '{CSV_DATEI}' wurde erstellt.")

# Funktion, um die CSV-Datei in eine Liste zu laden
def vokabeln_laden():
    vokabeln = []
    try:
        with open(CSV_DATEI, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Kopfzeile überspringen
            for row in reader:
                if len(row) == 2:
                    deutsch = row[0].strip().lower()  # Bereinigung
                    fremdsprache = row[1].strip().lower()
                    vokabeln.append((deutsch, fremdsprache))  # Tupel (Deutsch, Fremdsprache)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
    #gibt die Vokabeln als 2-Tupel-Liste zurück
    return vokabeln

# Funktion, um neue Vokabeln hinzuzufügen
def vokabel_hinzufuegen():
    while True:
        #strip sorgt dafür, dass alle Leerzeiche und großgeschriebene Buchstaben entfernt werden
        deutsch = input("Gib ein deutsches Wort ein (oder 'exit' zum Beenden): ").strip()
        if deutsch.lower() == "exit":
            break
        fremdsprache = input(f"Gib die Übersetzung von '{deutsch}' ein: ").strip()

        with open(CSV_DATEI, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([deutsch, fremdsprache])
        #Das f vor dem String sorgt dafür, dass Python die {}-Platzhalter im String durch Variablen ersetzt.
        #so würde es natürlich genauso gehen
        #print(" '" + deutsch + " - " + fremdsprache + "' wurde gespeichert!")
        print(f" '{deutsch} - {fremdsprache}' wurde gespeichert!")

# Funktion, um gespeicherte Vokabeln anzuzeigen
def vokabeln_anzeigen():
    vokabeln = vokabeln_laden()  # Vokabeln in Liste laden
    if not vokabeln:
        print("Keine Vokabeln vorhanden.")
        return

    print("\n Gespeicherte Vokabeln:")
    for deutsch, fremdsprache in vokabeln:
        print(f"{deutsch.capitalize()} - {fremdsprache.capitalize()}")

# Funktion, um Vokabeln zufällig abzufragen (mit `exit` zum Beenden)
def vokabel_trainer():
    vokabeln = vokabeln_laden()  # Vokabeln in Liste laden
    if not vokabeln:
        print("Keine Vokabeln vorhanden.")
        return

    random.shuffle(vokabeln)  # Zufällige Reihenfolge

    richtig = 0
    falsch = 0

    for deutsch, fremdsprache in vokabeln:
        antwort = input(f"Übersetze: {deutsch.capitalize()} (oder 'exit' zum Beenden) → ").strip().lower()
        if antwort == "exit":
            print("👋 Vokabeltraining beendet.")
            return  # Verlässt die Funktion direkt

        if antwort == fremdsprache:
            print("Richtig!")
            richtig += 1
        else:
            print(f"Falsch! Richtig wäre: {fremdsprache.capitalize()}")
            falsch += 1

    print(f"\n Ergebnis: {richtig} richtig, {falsch} falsch")

# Hauptmenü für den Vokabeltrainer
def hauptmenü():
    erstelle_csv_datei()  # Erstellt die Datei, falls sie nicht existiert

    while True:
        print("\n--- Vokabeltrainer ---")
        print("1. Vokabeln hinzufügen")
        print("2. Vokabeln trainieren")
        print("3. Gespeicherte Vokabeln anzeigen")
        print("4. Beenden")

        wahl = input("Wähle eine Option (1-4): ").strip()

        if wahl == "1":
            vokabel_hinzufuegen()
        elif wahl == "2":
            vokabel_trainer()
        elif wahl == "3":
            vokabeln_anzeigen()
        elif wahl == "4":
            print("Vokabeltrainer beendet.")
            sys.exit()  # Programm beenden
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")

# Starte das Programm
if __name__ == "__main__":
    hauptmenü()
