class Logger:
    def __init__(self, mensaje, n):
        self.mensaje = mensaje
        self.n = n

    def log_mensaje(self): #esta funcion abre un archivo en el que ecribe el mensaje pasado por parámetro
        f = open("fichero.txt", "w")
        f.write("start log" + '\n')
        for i in range(0,self.n):
            f.write(self.mensaje + '\n')
        f.write("end log:" + str(self.n) + "log(s)")
        f.close()
        return f

hola = Logger("buenas tardes", 4)
buenas_tardes = "buenas tardes"
ene = 4
print(hola.log_mensaje())
#llamar a logger en una funcion llamada de una clases Test
#class Test:
    #esta clase llama a la clase logger con una funcion
