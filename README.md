# Ejercicios_Clases_-de_POO

El grupo está formado por Ana López y Andrea Manuel. 
Nuestra dirección del repositorio de GitHub es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios_Clases_-de_POO.git)
https://github.com/andmansim/Ejercicios_Clases_-de_POO.git

Hemos realizado una serie de ejercicios, los cuales consiste en crear clases y trabajar con ellas.
El primer ejercicio es Palíndromo, método de clases. Su diagrama UML es el siguiente:

![diagrama uml metodo clases](/Palindromo/metodo_de_clases.jpg)

El segundo ejercicio es Palíndromo, método de instancia. Su diagrama UML es el siguiente:

![diagrama uml metodo instancia](/Palindromo/metodo_de_instancia.jpg)

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
```
