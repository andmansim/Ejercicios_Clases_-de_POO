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

#Segundo ejercicio
class Palindromo:
    
    def __init__(self, palabra):
        self.palabra = palabra
      
    def test(self):
        #quitar espacios
        if " " in self.palabra:
            self.palabra = self.palabra.replace(" ", "")

        #quitar toda parte acentuada

        if "á" in self.palabra:    
            self.palabra = self.palabra.replace("á", "a")
            
        if "é" in self.palabra:
            self.palabra = self.palabra.replace('é', 'e')

        if "í" in self.palabra:
            self.palabra = self.palabra.replace('í', 'i')

        if "ó" in self.palabra:
            self.palabra = self.palabra.replace('ó', 'o')
            
        if "ú" in self.palabra:
            self.palabra = self.palabra.replace('ú', 'u')

        #transformar toda letra mayúscula en minúscula
        self.palabra = self.palabra.lower()
            
        # invertir 
        f2 = ""
        for i in range(0, len(self.palabra)):
            f2 = self.palabra[i] + f2  # pasa la primera letra al final y la guarda en una nueva cadena     
        
        #Comparamos la frase inicial con el resultado y decimos si es o no
        
        if f2 == self.palabra:
            return True
        else:
            return False
    def __del__(self):
        print(self.palabra.upper())
```
El tercer ejercicio consiste en resolver una pregunta, cuya respuesta es la siguiente:
```
#El resultado del codigo proporcionado es:

#False
#0
#1
#2
#3
```
El último ejercicio es el de Logger. Su diagrama UML es el siguiente:

![diagrama uml logger](/Logger/loggerdrawio.jpg)

```
import logger

if __name__ == "__main__":
    print("¿Que mensaje quiere añadir en el archivo?")
    mensaje = input()
    print("¿Cuántas veces lo quiere añadir?")
    ene = int(input())
    testeo = logger.Test(mensaje, ene)
 
 class Logger:
    def __init__(self, mensaje, n):
        self.mensaje = mensaje
        self.n = n

    def log_mensaje(self): #esta funcion abre un archivo en el que ecribe el mensaje pasado por parámetro
        f = open("fichero.txt", "w")
        f.write("start log" + '\n')
        for i in range(0,int(self.n)):
            f.write(self.mensaje + '\n')
        f.write("end log:" + str(self.n) + "log(s)")
        f.close()
        return f

class Test:
    def __init__(self, mensaje, ene): #esta funcion constructor llama a la funcion de la clase logger
        mensajito = Logger(mensaje, ene)
        mensajito.log_mensaje()
        f = open("fichero.txt", "r")
        contador = 0
        for line in f:
            contador = contador + 1
            if contador <= ene + 2:
                print(line)
        f.close()
```
