import matplotlib.pyplot as plt

def create_pie_chart():
    # Daten für das Kreisdiagramm
    labels = ['Urlaub', 'Freunde besuchen', 'Zu Hause','Ehrenamt','Urlaub 2','Handwerk']
    sizes = [25, 20,30,10,10,5]
    colors = ['#FF5733', '#3498DB', '#2ECC71','#F1C40F','#9B59B6','#E67E22']
    explode = (0, 0, 0,0,0,0)  # Um den größten Teil des Kuchens hervorzuheben

    # Kreisdiagramm erstellen
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Stellt sicher, dass das Kreisdiagramm rund ist

    # Diagramm anzeigen
    plt.title("Ferienaktivitäten")
    plt.show()

# Funktion aufrufen, um das Diagramm zu erstellen
create_pie_chart()