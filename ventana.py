import tkinter as tk

class InterfazCalculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora ")
        #mensaje o resultado
        self.label = tk.Label(self.root, text="¡Hola desde la interfaz gráfica!",width=5,height=2,font=("Arial", 24),anchor="sw")#recorda que anchor hace referencia a los puntos cardinales para el posicionamiento del label
        #"ew" significa que el widget se expandirá horizontalmente para ocupar el espacio disponible en su columna (parecido a ocmbinar y centrar).
        self.label.grid(row=0, column=0, columnspan=4, sticky="we")
        self.mostrar_cuadricula()

    def mostrar_cuadricula(self):
        cont=7

        #Renglones
        for i in range(4):
            #columnas
            for j in range(4):
                #Colocar caracteres (/,*,-,+, y numeros ) en una posicion especifica 
                if(i == 3 and j==1):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                    label = tk.Label(frame, text="CLR",bg="grey", fg="white",font=("Helvetica", 24,"bold"))

                    #evento click izquierdo "<Button-1>"
                    # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
                    # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
                    label.bind("<Button-1>", lambda event: self.boton_click("CLR"))
                    frame.bind("<Button-1>",lambda event: self.boton_click("CLR"))

                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                elif(i==3 and j==2):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                    label = tk.Label(frame, text="=",bg="grey", fg="white",font=("Helvetica", 24,"bold"))

                    #evento click izquierdo "<Button-1>"
                    # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
                    # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
                    label.bind("<Button-1>", lambda event: self.boton_click("="))
                    frame.bind("<Button-1>",lambda event: self.boton_click("=")) 

                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                elif(i==0 and j==3):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                    label = tk.Label(frame, text="/",bg="grey", fg="white",font=("Helvetica", 24,"bold"))
                    
                    #evento click izquierdo "<Button-1>"
                    # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
                    # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
                    label.bind("<Button-1>", lambda event: self.boton_click("/"))
                    frame.bind("<Button-1>",lambda event: self.boton_click("/"))
                    
                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                elif(i==1 and j==3):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                    label = tk.Label(frame, text="*",bg="grey", fg="white",font=("Helvetica", 24,"bold"))

                    #evento click izquierdo "<Button-1>"
                    # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
                    # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
                    label.bind("<Button-1>", lambda event: self.boton_click("*"))
                    frame.bind("<Button-1>",lambda event: self.boton_click("*"))

                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                elif(i==2 and j==3):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                    label = tk.Label(frame, text="-",bg="grey", fg="white",font=("Helvetica", 24,"bold"))

                    #evento click izquierdo "<Button-1>"
                    # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
                    # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
                    label.bind("<Button-1>", lambda event: self.boton_click("-"))
                    frame.bind("<Button-1>",lambda event: self.boton_click("-"))

                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                elif(i==3 and j==3):
                    frame = tk.Frame(self.root, bg="grey", width=120, height=120)
                    label = tk.Label(frame, text="+",bg="grey", fg="white",font=("Helvetica", 24,"bold"))

                    #evento click izquierdo "<Button-1>"
                    # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
                    # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
                    label.bind("<Button-1>", lambda event: self.boton_click("+"))
                    frame.bind("<Button-1>",lambda event: self.boton_click("+"))

                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame                
                else:
                    frame = tk.Frame(self.root, bg="#e98c05", width=120, height=120)#cuadros donde va cada numero
                    label = tk.Label(frame, text=str(cont), fg="white", bg="#e98c05",font=("Helvetica", 24,"bold"))#establece numero en el label
                    
                    print(cont)

                    
                    
                    label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
                    #mostrar numeros en orden de teclado numerico 7894561230...
                    if(cont==9):
                        cont=4
                    elif(cont==6):
                        cont=1
                    elif(cont==3):
                        cont=0
                    else:       
                        label.bind("<Button-1>", lambda event: self.boton_click(str(cont)))
                        frame.bind("<Button-1>",lambda event: self.boton_click(str(cont)))
                        print("Print en el else"+str(cont))    
                        cont+=1
                frame.grid(row=i+1, column=j)# con bordes :frame.grid(row=i+1, column=j,padx=1, pady=1)
                #label.pack()

    def mostrar_ventana(self):
        # se ejecuta infinitamente para mostrar los eventos en la ventana
        self.root.mainloop()

    def boton_click(self,texto):
        print(texto)  

def main():
    ventana = InterfazCalculadora()
    ventana.mostrar_ventana()
if __name__ == "__main__":
    main()
