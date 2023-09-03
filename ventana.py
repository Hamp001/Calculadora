import tkinter as tk
from logica import aritmetica
class InterfazCalculadora:
 
    
    def __init__(self):
        #inciar objeto para el manejo de la logica y aritmetica
        self.aritmetica=aritmetica()
        self.botones_presionados=[]
        self.root = tk.Tk()
        self.root.title("Calculadora ")
        #mensaje o resultado
        self.label = tk.Label(self.root, text="0",width=5,height=2,font=("Arial", 24),anchor="sw")#recorda que anchor hace referencia a los puntos cardinales para el posicionamiento del label
        #"ew" significa que el widget se expandirá horizontalmente para ocupar el espacio disponible en su columna (parecido a ocmbinar y centrar).
        self.label.grid(row=0, column=0, columnspan=4, sticky="we")
        self.mostrar_cuadricula()

    def mostrar_cuadricula(self):
        #Renglones
        for i in range(4):
            #columnas
            for j in range(4):
                #Colocar caracteres (/,*,-,+, y numeros ) en una posicion especifica 
                #SIGNOS:
                if(i == 3 and j==1):
                    frame=self.establecerBoton("CLR","grey","white")
                elif(i==3 and j==2):
                    frame=self.establecerBoton("=","grey","white")
                elif(i==0 and j==3):
                    frame=self.establecerBoton("/","grey","white")
                elif(i==1 and j==3):
                    frame=self.establecerBoton("*","grey","white")
                elif(i==2 and j==3):
                    frame=self.establecerBoton("-","grey","white")
                elif(i==3 and j==3):
                    frame=self.establecerBoton("+","grey","white")    
                #NUMEROS:
                elif(i==0 and j==0):
                    frame=self.establecerBoton("7","#e98c05","white")
                elif(i==0 and j==1):
                    frame=self.establecerBoton("8","#e98c05","white")
                elif(i==0 and j==2):
                    frame=self.establecerBoton("9","#e98c05","white")
                elif(i==1 and j==0):
                    frame=self.establecerBoton("4","#e98c05","white")
                elif(i==1 and j==1):
                    frame=self.establecerBoton("5","#e98c05","white")
                elif(i==1 and j==2):
                    frame=self.establecerBoton("6","#e98c05","white")
                elif(i==2 and j==0):
                    frame=self.establecerBoton("1","#e98c05","white")
                elif(i==2 and j==1):
                    frame=self.establecerBoton("2","#e98c05","white")
                elif(i==2 and j==2):
                    frame=self.establecerBoton("3","#e98c05","white")
                elif(i==3 and j==0):
                    frame=self.establecerBoton("0","#e98c05","white")

                frame.grid(row=i+1, column=j)# con bordes :frame.grid(row=i+1, column=j,padx=1, pady=1)
                #label.pack()

    def mostrar_ventana(self):
        # se ejecuta infinitamente para mostrar los eventos en la ventana
        self.root.mainloop()
    
    def establecerBoton(self,nombreBoton,colorBg,colorFg):
        frame = tk.Frame(self.root, bg=colorBg, width=120, height=120)
        label = tk.Label(frame, text=nombreBoton,bg=colorBg, fg=colorFg,font=("Helvetica", 24,"bold"))

        #evento click izquierdo "<Button-1>"
        # En este caso, estamos creando una función anonima (lambda) que toma un parámetro llamado event.
        # Esta función lambda se utilizará como la función que se ejecutará cuando ocurra el evento
        label.bind("<Button-1>", lambda event: self.Boton_click(nombreBoton))
        frame.bind("<Button-1>",lambda event: self.Boton_click(nombreBoton))

        #efecto hover sobre el label y el frame
        frame.bind("<Enter>",lambda event: (frame.config(bg="#4e4b47"),label.config(bg="#4e4b47")) )
        frame.bind("<Leave>",lambda event: (frame.config(bg=colorBg),label.config(bg=colorBg,fg=colorFg)))

        label.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el label en el centro del frame
        return frame
    
    def Boton_click(self,nombreBoton):
        
        if(nombreBoton=="CLR"):
            self.label.config(text="0")
            self.botones_presionados.clear()
            return
        
        self.mostrarEnPantalla(nombreBoton)   

        if(nombreBoton=="="):
            self.mostrarEnPantalla(texto=str(self.aritmetica.getResultado()))
            self.label.config(text=str(self.aritmetica.getResultado()))
            self.botones_presionados.clear()
            #hacer perdurar el resultado para poder hacer operaciones proximamente
            self.botones_presionados.append(str(self.aritmetica.getResultado()))


    def mostrarEnPantalla(self,texto):
        self.botones_presionados.append(texto)
        texto_mostrado = "".join(self.botones_presionados)  # Convierte la lista en una cadena  
        self.label.config(text=texto_mostrado)

        self.aritmetica.setCaracteresIngresados(texto_mostrado)


    