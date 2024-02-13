from collections import deque
import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def bfs_shortest_path(graph, start, goal):
    # Inicializar la cola para el BFS
    queue = deque([(start, [start])])
    # Mientras haya nodos en la cola
    while queue:
        # Sacar el nodo actual y el camino hasta este nodo
        current_node, current_path = queue.popleft()
        # Si el nodo actual es el nodo objetivo, retornar el camino
        if current_node == goal:
            return current_path
        # Para cada vecino del nodo actual
        for neighbor in graph.neighbors(current_node):
            # Si el vecino no ha sido visitado
            if neighbor not in current_path:
                # Agregar el vecino a la cola con el camino actualizado
                queue.append((neighbor, current_path + [neighbor]))

def dibujar_metro_amsterdam(start_node, end_node):
    # Crear un grafo dirigido para representar las conexiones del metro
    G = nx.Graph()

    # Agregar estaciones al grafo
    estaciones = {
        'Isolatorweg': (0, 0),
        'Sloterdijk': (2, 1),
        'De Vlugtlaan': (3, 0),
        'Jan van Galenstraat': (1, -1),
        'Postjesweg': (-1, -1),
        'Lelylaan': (-2, 0),
        'Heemstedestraat': (-1, 2),
        'Henk Sneevlietweg': (2, -2),
        'Amstelveenseweg': (-3, 1),
        'Zuid': (3, -2),
        'RAI': (0, 3),
        'Overamstel': (4, 0),
        'Duivendrecht': (-3, -3),
        'Strandvliet': (1, 3),
        'Biljmer ArenA': (5, 2),
        'Bullewijk': (-4, 2),
        'Holendrecht': (0, -4),
        'Reigersbos': (3, 4),
        'Gein': (-2, -4),
        'Van der Madeweg': (4, -3),
        'Spaklerweg': (-5, 1),
        'Amstel': (-1, 4),
        'Wibautstraat': (2, -5),
        'Weesperplein': (4, 4),
        'Waterlooplein': (0, 5),
        'Nieuwmarkt': (-4, 4),
        'Centraal Station': (5, -4),
        'Gaasperplas': (-5, -2),
        'Kraaiennest': (1, 6),
        'Gazenhoef': (-2, 6),
        'Verrijn Stuartweg': (5, 5),
        'Diemen Zuid': (-6, 0),
        'Verserpolder': (4, -5),
        'Europaplein': (2, 7),
        'De Pijp': (-5, 6),
        'Vijzelgracht': (6, 1),
        'Rokin': (-3, -6),
        'Noorderark': (7, 0),
        'Noord': (-6, 3),
    }
    G.add_nodes_from(estaciones)

    # Agregar conexiones entre estaciones (conexiones ficticias)
    conexiones = [

        # LINEA VERDE
        ('Isolatorweg', 'Sloterdijk'),
        ('Sloterdijk', 'De Vlugtlaan'),
        ('De Vlugtlaan', 'Jan van Galenstraat'),
        ('Jan van Galenstraat', 'Postjesweg'),
        ('Postjesweg', 'Lelylaan'),
        ('Lelylaan', 'Heemstedestraat'),
        ('Heemstedestraat', 'Henk Sneevlietweg'),
        ('Henk Sneevlietweg', 'Amstelveenseweg'),
        ('Amstelveenseweg', 'Zuid'),
        ('Zuid', 'RAI'),
        ('RAI', 'Overamstel'),
        ('Overamstel', 'Van der Madeweg'),
        ('Van der Madeweg', 'Duivendrecht'),
        ('Duivendrecht','Strandvliet'),
        ('Strandvliet','Biljmer ArenA'),
        ('Biljmer ArenA','Bullewijk'),
        ('Bullewijk','Holendrecht'),
        ('Holendrecht','Reigersbos'),
        ('Reigersbos','Gein'),
        #

        #LINEA NARANJA
        ('Overamstel', 'Spaklerweg'),
        ('Spaklerweg', 'Amstel'),
        ('Amstel', 'Wibautstraat'),
        ('Wibautstraat', 'Weesperplein'),
        ('Weesperplein', 'Waterlooplein'),
        ('Waterlooplein', 'Nieuwmarkt'),
        ('Nieuwmarkt', 'Centraal Station'),
        #

        #LINEA AZUL
        ('Zuid', 'Europaplein'),
        ('Europaplein', 'De Pijp'),
        ('De Pijp', 'Vijzelgracht'),
        ('Vijzelgracht', 'Rokin'),
        ('Centraal Station', 'Noorderark'),
        ('Noorderark', 'Noord'),
        ('Rokin', 'Centraal Station'),
        #

        #LINEA ROJA
        ('Van der Madeweg', 'Verserpolder'),
        ('Verserpolder', 'Diemen Zuid'),
        ('Diemen Zuid', 'Verrijn Stuartweg'),
        ('Verrijn Stuartweg', 'Gazenhoef'),
        ('Gazenhoef', 'Kraaiennest'),
        ('Kraaiennest', 'Gaasperplas'),
        #

    ]
    G.add_edges_from(conexiones)

    # Definir manualmente las posiciones de los nodos
    pos = {
        'Isolatorweg': (-12, 12),
        'Sloterdijk': (-12, 10.50),
        'De Vlugtlaan': (-12, 9),
        'Jan van Galenstraat': (-12, 7.5),
        'Postjesweg': (-12, 6),
        'Lelylaan': (-12, 4.5),
        'Heemstedestraat': (-12, 3),
        'Henk Sneevlietweg': (-12, 1.5),
        'Amstelveenseweg': (-10.92,-0.15),
        'Zuid': (-9.78,-0.15),
        'RAI': (-8.63, -0.22),
        'Overamstel': (-7.34, -0.20),
        'Duivendrecht' : (-6.26, -1.74),
        'Strandvliet' : (-6.27, -3.57),
        'Biljmer ArenA' : (-6.23, -5.31),
        'Bullewijk' : (-6.30, -6.92),
        'Holendrecht' : (-6.33, -8.51),
        'Reigersbos' : (-5.12, -8.45),
        'Gein' : (-3.93, -8.37),
        'Van der Madeweg' : (-6.30, -0.51),
        'Spaklerweg' : (-6.35, 1.17),
        'Amstel' : (-6.36, 2.85),
        'Wibautstraat' : (-6.37, 4.25),
        'Weesperplein' : (-6.43, 5.8),
        'Waterlooplein' : (-6.40, 7.26),
        'Nieuwmarkt' : (-6.37, 8.68),
        'Centraal Station' : (-7.24, 10.44),
        'Gaasperplas' : (-0.41, -8.17),
        'Kraaiennest' : (-0.49, -6.46),
        'Gazenhoef' : (-0.52, -4.53),
        'Verrijn Stuartweg' : (-0.55, -3.26),
        'Diemen Zuid' : (-2.32, -1.88),
        'Verserpolder' : (-5, -1.6),
        'Europaplein' : (-8.69, 1.35),
        'De Pijp' : (-8.69, 3),
        'Vijzelgracht' : (-8.69, 6.21),
        'Rokin' : (-8.02, 8.66),
        'Noorderark' : (-5.97, 12.93),
        'Noord' : (-5.14, 14.15),
    }

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, edge_color='gray', arrowsize=20)

    # Resaltar el nodo inicial y final
    nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[end_node], node_color='red', node_size=700)

    # Calcular el camino más corto entre el nodo de inicio y el nodo destino
    shortest_path = bfs_shortest_path(G, start_node, end_node)
    path_with_arrows = " ➔ ".join(shortest_path)

    # Resaltar el camino más corto en rojo
    edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

    plt.text(-13, 16, "Ruta más corta:")
    plt.text(-13, 15.5, path_with_arrows)

    # Mostrar el dibujo
    plt.show()

def buscar_ruta():
    try:
        estacionInicial = combo_estacion_inicial.get()
        estacionFinal = combo_estacion_final.get()

        dibujar_metro_amsterdam(estacionInicial, estacionFinal)
    except:
        messagebox.showerror('ERROR', 'HA OCURRIDO UN ERROR')

def actualizar_precio(event):
    indice = combo_billete.current()  # Obtener el índice del billete seleccionado
    if indice >= 0:  # Verificar si se seleccionó un billete
        billetePrecio.config(state="normal")
        precioMxTxt.config(state="normal")
        billete_seleccionado = billetes[indice]  # Obtener el billete correspondiente
        precio = billete_seleccionado.precio  # Obtener el precio del billete
        precioMX = precio * 18.39
        
        billetePrecio.delete(0, tk.END)  # Limpiar el contenido actual de la caja de texto
        billetePrecio.insert(0, f"{precio:.2f} Euros")  # Insertar el precio en la caja de texto

        precioMxTxt.delete(0, tk.END)  # Limpiar el contenido actual de la caja de texto
        precioMxTxt.insert(0, f"{precioMX:.2f} Pesos")  # Insertar el precio en la caja de texto

        billetePrecio.config(state="readonly")
        precioMxTxt.config(state="readonly")

def mostrar_ayuda():

    ventana = tk.Toplevel(root)
    ventana.title("Ayuda")

    mensaje = "Esta es una representación del mapa del metro de Ámsterdam.\n" \
              "Seleccione una estación inicial y una estación final y haga clic en 'Mostrar Ruta' para encontrar la ruta más corta entre ellas. \n" \
              "Además, seleccione el billete que usará y se verá tanto el precio en Euros como en Pesos Mexicanos \n" \
              "La estación inicial será representada como un circulo VERDE y la estación final como un circulo ROJO"
    lblAyuda = tk.Label(ventana, text=mensaje)
    lblAyuda.pack()

    lblCirculoVerde = tk.Canvas(ventana, width=150, height=30)
    lblCirculoVerde.pack()
    lblCirculoVerde.create_oval(5, 5, 25, 25, fill="green")
    lblCirculoVerde.create_text(40, 15, text="Estación Inicial", anchor=tk.W)

    lblCirculoRojo = tk.Canvas(ventana, width=150, height=30)
    lblCirculoRojo.pack()
    lblCirculoRojo.create_oval(5, 5, 25, 25, fill="red")
    lblCirculoRojo.create_text(40, 15, text="Estación Final", anchor=tk.W)

nombres_estaciones = [
    'Isolatorweg', 'Sloterdijk', 'De Vlugtlaan', 'Jan van Galenstraat',
    'Postjesweg', 'Lelylaan', 'Heemstedestraat', 'Henk Sneevlietweg',
    'Amstelveenseweg', 'Zuid', 'RAI', 'Overamstel', 'Duivendrecht',
    'Strandvliet', 'Biljmer ArenA', 'Bullewijk', 'Holendrecht',
    'Reigersbos', 'Gein', 'Van der Madeweg', 'Spaklerweg', 'Amstel',
    'Wibautstraat', 'Weesperplein', 'Waterlooplein', 'Nieuwmarkt',
    'Centraal Station', 'Gaasperplas', 'Kraaiennest', 'Gazenhoef',
    'Verrijn Stuartweg', 'Diemen Zuid', 'Verserpolder', 'Europaplein',
    'De Pijp', 'Vijzelgracht', 'Rokin', 'Noorderark', 'Noord'
]

class Billetes:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre

billete1 = Billetes("Sencillo", 3.20)
billete2 = Billetes("1 Dia", 7.50)
billete3 = Billetes("2 Dias", 12)
billete4 = Billetes("3 Dias", 16)
billete5 = Billetes("4 Dias", 20.5)
billete6 = Billetes("5 Dias", 25)
        
billetes = [
    billete1,
    billete2,
    billete3,
    billete4,
    billete5,
    billete6
]

# Crear la ventana principal
root = tk.Tk()
root.title("LMAmsterdam")
root.geometry("300x600")
root.config(bg="white")

logo = tk.PhotoImage(file="LOGO.PNG")
labelLogo = tk.Label(image=logo, bg="white")
labelLogo.pack(pady=5)

btn_ayuda = tk.Button(root, text="Ayuda", command=mostrar_ayuda, bg="#53A548", fg="white")
btn_ayuda.pack(side="top", anchor="ne", padx=10, pady=10)

# ComboBox para seleccionar la estación inicial
labelEstacionInicial = tk.Label(root, text="Estacion Inicial", bg="white")
labelEstacionInicial.pack()
combo_estacion_inicial = ttk.Combobox(root, values=nombres_estaciones, width=25)
combo_estacion_inicial.set("Seleccionar estación inicial")
combo_estacion_inicial.bind("<<ComboboxSelected>>", buscar_ruta)
combo_estacion_inicial.pack(pady=5)

# ComboBox para seleccionar la estación final
labelEstacionFinal = tk.Label(root, text="Estacion Final", bg="white")
labelEstacionFinal.pack()
combo_estacion_final = ttk.Combobox(root, values=nombres_estaciones, width=25)
combo_estacion_final.set("Seleccionar estación final")
combo_estacion_final.bind("<<ComboboxSelected>>", buscar_ruta)
combo_estacion_final.pack(pady=5)

labelBillete = tk.Label(root, text="Billete", bg="white")
labelBillete.pack()
combo_billete = ttk.Combobox(root, values=[str(billete) for billete in billetes], width=25)
combo_billete.set("Seleccionar billete")
combo_billete.pack(pady=5)
combo_billete.bind("<<ComboboxSelected>>", actualizar_precio)

labelEuros = tk.Label(root, text="Precio en Euros", bg="white")
labelEuros.pack()
billetePrecio = tk.Entry(root, state="readonly")
billetePrecio.pack()

labelMX = tk.Label(root, text="Precio en Pesos Mexicanos", bg="white")
labelMX.pack()
precioMxTxt = tk.Entry(root, state="readonly")
precioMxTxt.pack()

# Botón para iniciar el dibujo del metro
btn_dibujar_metro = tk.Button(root, text="Mostrar Ruta", command=buscar_ruta, bg="#3E92CC", fg="white", width=20, height=2)
btn_dibujar_metro.pack(pady=30)

# Ejecutar la aplicación
root.mainloop()



