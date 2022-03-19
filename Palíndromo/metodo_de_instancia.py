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
        
#creando instancias
p = Palindromo("radar")
print(p.test())
p = Palindromo("sonar")
print(p.test()) 

