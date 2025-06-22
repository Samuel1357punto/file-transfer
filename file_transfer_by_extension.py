import os
import shutil
import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox


def boton_continuar():
    extension = entrada_extension.get()
    ruta_origen = entrada_ruta_origen.get()
    ruta_destino = entrada_ruta_destino.get()
    print(extension)
    print(ruta_origen)
    print(ruta_destino)
    contador = 0

    for archivo in os.listdir(ruta_origen):
        if archivo.endswith(extension):
            origen = os.path.join(ruta_origen, archivo)  # Ruta de cada archivo de las carpetas
            destino = os.path.join(ruta_destino, archivo)
            shutil.move(origen, destino)  # Mueve el archivo de una carpeta a otra
            messagebox.showinfo("Éxito", "¡Archivos movidos correctamente!")
            contador += 1

def seleccionar_carpeta():
    ruta = filedialog.askdirectory(title="Selecciona la carpeta de origen")
    if ruta:
        entrada_ruta_origen.delete(0, tk.END)
        entrada_ruta_origen.insert(0, ruta)

def seleccionar_carpeta2():
    ruta = filedialog.askdirectory(title="Selecciona la carpeta de origen")
    if ruta:
        entrada_ruta_destino.delete(0, tk.END)
        entrada_ruta_destino.insert(0, ruta)

ventana = tk.Tk()
ventana.geometry("900x500")

ventana.title("Transferencia de archivos por extensión")

extension = "."
ruta_origen = "/"
ruta_destino = "/"

#Carpeta origen
tk.Label(ventana, text="Selecciona la carpeta de origen").pack(pady=5)
entrada_ruta_origen = tk.Entry(ventana, width=70)
entrada_ruta_origen.pack(pady=10)
tk.Button(ventana, text="Buscar carpeta", command=seleccionar_carpeta).pack(pady=5)

#Carpeta destino
tk.Label(ventana, text="Selecciona la carpeta de destino").pack(pady=5)
entrada_ruta_destino = tk.Entry(ventana, width=70)
entrada_ruta_destino.pack(pady=10)
tk.Button(ventana, text="Buscar carpeta", command=seleccionar_carpeta2).pack(pady=5)

#Extensión
tk.Label(ventana, text="Extensión de los archivos que quieres mover").pack(pady=5)
entrada_extension = tk.Entry(ventana, width=10)
entrada_extension.pack(pady=10)

tk.Button(ventana, text="Trasnferir", command=boton_continuar).pack(pady=5)

ventana.mainloop()


"""

extension = input("¿Cuál es la extensión de los archivos que quieres mover a esta carpeta?")
nueva_carpeta = f"Archivos_{extension}" #Nombre de la carpeta que se creare

if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta) #Se crea la carpeta
    print(f"Carpeta '{nueva_carpeta}' creada.")
    

ruta_origen = input("Escribe la ruta completa del archivo")
carpeta_origen = "C:\\Users\\Sam\\PycharmProjects\\Automatizacion\\archivos" #Ruta de la carpeta de origen
contador = 0

-----------------------------------------------------------------------------------------------------------------------

for archivo in os.listdir(carpeta_origen):
    if archivo.endswith(".html"):
        origen = os.path.join(carpeta_origen, archivo) #Ruta de cada archivo de las carpetas
        destino = os.path.join(nueva_carpeta, archivo)
        shutil.move(origen, destino) #Mueve el archivo de una carpeta a otra
        contador += 1

print (f"Se movieron {contador} archivos a la carpeta '{nueva_carpeta}'.")

"""