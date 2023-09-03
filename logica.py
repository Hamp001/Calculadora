class aritmetica():

    def __init__(self):
        self.caracteresIngresados=[]
        self.resultado=0
        self.escuchar()

    def getCaracteresIngresados(self):
        return self.caracteresIngresados
    
    def setCaracteresIngresados(self,texto_mostrado):
        self.caracteresIngresados=texto_mostrado
        self.escuchar()

    def setResultado(self,resultado):
        self.resultado=resultado

    def getResultado(self):
        return self.resultado

    def escuchar(self):
        print(f"Boton presionado: {self.getCaracteresIngresados()}")
        if "=" in self.getCaracteresIngresados():# verificar si = esta presente en la lista
            operacion = self.getCaracteresIngresados().split("=")[0] # separamos la operacion en funcion del igual
            try:
                #toma la cadena de texto operacion y la evalúa como una expresión de Python. En este caso,
                #Python interpreta la cadena como una expresión matemática y realiza los cálculos correspondientes.
                
                #si operacion fuera igual a "2 + 3 * 4", después de ejecutar resultado = eval(operacion),
                #la variable resultado contendría el valor 14, que es el resultado de la expresión.
                resultado = eval(operacion)
                self.setResultado(resultado)
                print(f"El resultado es = {self.getResultado()}")
            except Exception as e:
                #Puede dar error si no encuentra una espresion matematica como es el caso de CLR
                print(f"Error en la operación: {e}")
        else:
            print("Esperando operación...")



