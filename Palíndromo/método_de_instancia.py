#Segundo ejercicio
class Palindromo():
    
    def esPalindromo(f):
        #quitar espacios
        if " " in f:
            f = f.replace(" ", "")

        #quitar toda parte acentuada

        if "á" in f:    
            f = f.replace("á", "a")
            
        if "é" in f:
            f = f.replace('é', 'e')

        if "í" in f:
            f = f.replace('í', 'i')

        if "ó" in f:
            f = f.replace('ó', 'o')
            
        if "ú" in f:
            f = f.replace('ú', 'u')

        #transformar toda letra mayúscula en minúscula
        f = f.lower()
            
        # invertir 
        f2 = ""
        for i in range(0, len(f)):
            f2 = f[i] + f2  # pasa la primera letra al final y la guarda en una nueva cadena     
     
        #Comparamos la frase inicial con el resultado y decimos si es o no
        if f2 == f:
            return True
        else:
            return False


print(Palindromo.esPalindromo("Os ó"))