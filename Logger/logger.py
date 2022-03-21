class Logger:
    def log_mensaje(mensaje, n): #esta funcion abre un archivo en el que ecribe el mensaje pasado por parámetro
        f = open("fichero.txt", "w")
        f.write("start log")
        for i in range(1,n):
            f.write(mensaje + '\n')
        f.write("end log:" + str(n) + "log(s)")
        f.close()
        return f

    #escribe mensaje dado como archivo cada vez que se llame a la funcion log_mensaje.
    #primera linea archivo: start log
    #ultima linea de archivo: end log:xlog(s) (cuando se destruye la instancia)
    #x -> cuantas veces se ha llamado a la funcion log
hola = Logger()
buenas_tardes = "buenas tardes"
ene = 4
fichero = hola.log_mensaje(buenas_tardes, ene)
print(fichero)
#llamar a logger en una funcion llamada de una clases Test
#class Test:
    #esta clase llama a la clase logger con una funcion
