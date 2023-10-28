from ventana import InterfazCalculadora
def main():
    calculadora=InterfazCalculadora(
        colorBgSignos="grey",
        colorBgNumeros="#e98c05",
        colorFg="white",
        colorEnterMouse="#4e4b47")
    """"
    calculadora=ventana.InterfazCalculadora(
        colorBgSignos="grey",
        colorBgNumeros="#5ac2be",
        colorFg="white",
        colorEnterMouse="#4e4b47")
    """
    calculadora.mostrar_ventana()
    """
    FALTA:
    1.Agregar boton para punto y parentesis
    2.Agregar boton para borrar un solo caracter
    3.Que acepte entrada tambien con el teclado, (presionando numeros) 
    """
if __name__ == "__main__":
    main()
