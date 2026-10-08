import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora gravedad quemaduras")
ventana.geometry("900x700")

titulo = tk.Label(ventana, text="Selecciona la zona del cuerpo de la quemadura", font=("Arial", 20))
titulo.pack(pady=20)
frame_botones = tk.Frame(ventana)
frame_botones.pack()
zonas = {"Cara", "Cuello", "Manos", "Pies", "Tronco", "Piernas"}
for zona in zonas:
    tk.Button(frame_botones, text=zona, width=15).pack(side=tk.LEFT, padx=5)

label_SCQ = tk.Label(ventana, text="Selecciona el porcentaje de quemadura", font=("Arial", 20))
label_SCQ.pack(pady=20)
percentaje_SCQ = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL)

label_age = tk.Label(ventana, text="Selecciona la edad del paciente", font=("Arial", 20))
label_age.pack(pady=20)
age = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL)

boton_aceptar = tk.Button(ventana, text="Aceptar", font=("Arial", 20), command=lambda: print(f"Zona: {zona}, Porcentaje: {percentaje_SCQ.get()}, Edad: {age.get()}"))
boton_aceptar.pack(pady=20)

equation = 


ventana.mainloop()