class aritmetica():

    def __init__(self):
        self.caracteresIngresados=[]
        self.escuchar()

    def getCaracteresIngresados(self):
        return self.caracteresIngresados
    
    def setCaracteresIngresados(self,texto_mostrado):
        self.caracteresIngresados=texto_mostrado
        self.escuchar()

    def escuchar(self):
        print(f"Boton presionado: {self.getCaracteresIngresados()}")

