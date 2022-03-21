# Ejercicios_Clases_-de_POO

El grupo está formado por Ana López y Andrea Manuel. 
Nuestra dirección del repositorio de GitHub es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios_Clases_-de_POO.git)
https://github.com/andmansim/Ejercicios_Clases_-de_POO.git

Hemos realizado una serie de ejercicios, los cuales consiste en crear clases y trabajar con ellas.
El primer ejercicio es Palíndromo, método de clases. Su diagrama UML es el siguiente:

![diagrama uml metodo clases](/Palindromo/metodo_de_clase.jpg)

El segundo ejercicio es Palíndromo, método de instancia. Su diagrama UML es el siguiente:

![diagrama uml metodo instancia](/Palindromo/metodo-de-instancia.jpg)

```
import metodo_de_clase
import metodo_de_instancia


if __name__=="__main__":
    print("¿Qué ejercicio quiere realizar, 1.Método de clase, 2.Método de instancia?" + " 1 / 2")
    user = int(input())
    
    if user == 1:
        print(metodo_de_clase.Palindromo.esPalindromo("Os ó"))
    elif user == 2:
        
        a = metodo_de_instancia.Palindromo("radar")
        print(a.test())

    else:
        print("Por favor elija entre 1 y 2")
        
 Primer ejercicio
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
```
