import matplotlib.pyplot as plt

def create_pie_chart():
    # Daten für das Kreisdiagramm
    labels = ['Schlaf', 'tanzen', "kroatien" , "freunde und familie treffen" , "an carl denken","essen","schwimmen"]
    sizes = [20, 5, 15 ,15,30,10,5]
    colors = ['#ff9999', '#66b3ff', '#99ff99',"#7344b7","#a1eb8d","#cd2c41","#b9e3ea"]
    explode = (0, 0, 0,0,0,0,0)  # Um den größten Teil des Kuchens hervorzuheben

    # Kreisdiagramm erstellen
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Stellt sicher, dass das Kreisdiagramm rund ist

    # Diagramm anzeigen
    plt.title("Tagesaktivitäten")
    plt.show()

# Funktion aufrufen, um das Diagramm zu erstellen
create_pie_chart()