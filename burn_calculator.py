import tkinter as tk
from tkinter import messagebox


def calcular_gravedad(zona, porcentaje, edad, grado):
    zonas_graves = {"Cara", "Cuello", "Manos", "Pies",
                    "Genitales", "Articulaciones", "Pies", "Manos"}
    
    if grado == 1:
        gravedad = "Leve"
    
    elif grado == 2:
        if zona in zonas_graves:
            if porcentaje > 10:
                gravedad = "Grave"
            else:
                gravedad = "Moderada"
        else:
            if porcentaje < 10:
                gravedad = "Leve"
            elif porcentaje < 25:
                if edad < 10 or edad > 60:
                    gravedad = "Grave"
                else:
                    gravedad = "Moderada"
            else:
                gravedad = "Grave"
    
    elif grado == 3:
        if porcentaje > 1:
            gravedad = "Grave"
        else:
            gravedad = "Moderada"
    
    resultado = f"Zona: {zona}\nPorcentaje: {porcentaje}%\nEdad: {edad}\nGrado: {grado}\nGravedad: {gravedad}"
    messagebox.showinfo("Resultado", resultado)

ventana = tk.Tk()
ventana.title("Burn severity calculator")
ventana.geometry("900x1100")

zona_seleccionada = tk.StringVar()
grado_seleccionado = tk.IntVar()

zonas_graves = {"Cara", "Cuello", "Manos", "Pies", "Genitales", "Articulaciones", "Pies", "Manos"}
zonas_normales = {"Brazos", "Espalda", "Abdomen"}

label_zona = tk.Label(ventana, text="Select the burn area", font=("Arial", 20))
label_zona.pack(pady=10)

# --------------------------------------- Zona botones ---------------------------------------
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Zonas graves
frame_graves = tk.LabelFrame(frame_botones, text = "CRITICAL ZONES", font = ("Arial", 10, "bold"), fg = "red")
frame_graves.pack(side=tk.LEFT, padx=10)
for zona in zonas_graves:
    boton = tk.Button(frame_graves, text=zona, font=("Arial", 15), command=lambda z=zona: zona_seleccionada.set(z))
    boton.pack(pady=5)
    
# Zonas normales
frame_normales = tk.LabelFrame(frame_botones, text="NORMAL ZONES",
                        font=("Arial", 10, "bold"), fg="yellow")
frame_normales.pack(side=tk.LEFT, padx=10)
for zona in zonas_normales:
    boton = tk.Button(frame_normales, text=zona, font=(
        "Arial", 15), command=lambda z=zona: zona_seleccionada.set(z))
    boton.pack(pady=5)

# Porcentaje SCQ
label_SCQ = tk.Label(ventana, text="Enter the percentage of burned area (%)", font=("Arial", 20))
label_SCQ.pack(pady=10)

percentaje_SCQ = tk.Entry(ventana, font=("Arial", 20))
percentaje_SCQ.pack(pady=10)

# Edad del paciente
entry_age = tk.Label(ventana, text="Enter the age of the pacient", font=("Arial", 20))
entry_age.pack(pady=10)

entry_age = tk.Entry(ventana, font=("Arial", 20))
entry_age.pack(pady=10)

# Grado de la quemadura
label_grado = tk.Label(ventana, text="Select burn degree", font=("Arial", 20))
label_grado.pack(pady=10)

frame_grado = tk.Frame(ventana)
frame_grado.pack(pady=10)

grados_info = {
    1: "Degree 1: First degree burn (superficial)",
    2: "Degree 2: Second degree burn (partial thickness)",
    3: "Degree 3: Third degree burn (full thickness)"
}

for grado, info in grados_info.items():
    boton = tk.Radiobutton(frame_grado, text=info, variable=grado_seleccionado, value=grado, font=("Arial", 15))
    boton.pack(anchor=tk.W, padx=20, pady=5)

# Calcular gravedad
boton_calcular = tk.Button(ventana, text="CALCULATE", font=("Arial", 18, "bold"),
                           bg="lightblue", command=lambda: calcular_gravedad(
                              zona_seleccionada.get(),
                              float(percentaje_SCQ.get()),
                              int(entry_age.get()),
                              grado_seleccionado.get()),
                           width=20, height=2)
boton_calcular.pack(pady=30)


ventana.mainloop()