import tkinter as tk

class InterfazGrafica:
    def __init__(self, nombre_ventana):
        self.nombre_ventana = nombre_ventana
        self.root = tk.Tk()
        self.root.title(nombre_ventana)

        self.label = tk.Label(self.root, text="¡Hola desde la interfaz gráfica!",width=5,height=2,font=("Helvetica", 16),anchor="w")
        #"ew" significa que el widget se expandirá horizontalmente para ocupar el espacio disponible en su columna.
        self.label.grid(row=0, column=0, columnspan=5, sticky="ew")
        self.mostrar_cuadricula()

    def mostrar_cuadricula(self):
        cont=7
        for i in range(4):
            for j in range(4):
                #colorear esquina inferior derecha e izquierda 
                if(i == 3 and (j == 2 or j==1)):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                elif(i==0 and j==3):
                    frame = tk.Frame(self.root, bg="white", width=120, height=120)
                    label = tk.Label(frame, text="/", fg="black",font=("Helvetica", 24))
                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                    
                elif(i==1 and j==3):
                    frame = tk.Frame(self.root, bg="white", width=120, height=120)
                    label = tk.Label(frame, text="*", fg="white", bg="blue",font=("Helvetica", 24))
                elif(i==2 and j==3):
                    frame = tk.Frame(self.root, bg="white", width=120, height=120)
                    label = tk.Label(frame, text="+", fg="white", bg="blue",font=("Helvetica", 24))
                elif(i==3 and j==3):
                    frame = tk.Frame(self.root, bg="white", width=120, height=120)
                    label = tk.Label(frame, text="-", fg="white", bg="blue",font=("Helvetica", 24))
                else:
                    frame = tk.Frame(self.root, bg="#e98c05", width=120, height=120)#cuadros donde va cada numero
                    label = tk.Label(frame, text=str(cont), fg="white", bg="#e98c05",font=("Helvetica", 24))#establece numero en el label
                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                    #mostrar numeros en orden de teclado numerico 7894561230...
                    if(cont==9):
                        cont=4
                    elif(cont==6):
                        cont=1
                    elif(cont==3):
                        cont=0
                    else:           
                        cont+=1
                
                frame.grid(row=i+1, column=j)# con bordes :frame.grid(row=i+1, column=j,padx=1, pady=1)
                #label.pack()

    def mostrar_ventana(self):
        # se ejecuta infinitamente para mostrar los eventos en la ventana
        self.root.mainloop()


def main():
    ventana = InterfazGrafica("Calculadora")
    ventana.mostrar_ventana()
if __name__ == "__main__":
    main()
