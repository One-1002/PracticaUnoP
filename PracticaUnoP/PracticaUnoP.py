import tkinter as tk
pantalla= tk.Tk()
pantalla.title("Hola mundo")
pantalla.geometry("560x480")
boton=tk.Button(pantalla,text="Hola, Mundo")
boton.place(x=50, y=50)
Entrada= tk.Entry()
Entrada.place(x=50,y=160, width=150)
pantalla.mainloop()
