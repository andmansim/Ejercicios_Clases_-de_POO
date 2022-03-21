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


print("¿Que mensaje quiere añadir en el archivo?")
mensaje = input()
print("¿Cuántas veces lo quiere añadir?")
ene = int(input())
mensajito = Logger(mensaje, ene)
mensajito.log_mensaje()
f = open("fichero.txt", "r")
contador = 0
for line in f:
    contador = contador + 1
    if contador <= ene + 2:
        print(line)
f.close()
#llamar a logger en una funcion llamada de una clases Test
#class Test:
    #esta clase llama a la clase logger con una funcion
