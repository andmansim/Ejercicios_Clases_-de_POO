import logger

if __name__ == "__main__":
    print("¿Que mensaje quiere añadir en el archivo?")
    mensaje = input()
    print("¿Cuántas veces lo quiere añadir?")
    ene = int(input())
    testeo = logger.Test(mensaje, ene)