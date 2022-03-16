import metodo_de_clase


if __name__=="__main__":
    print("¿Qué ejercicio quiere realizar, 1.Método de clase, 2.Método de instancia?" + " 1 / 2")
    user = int(input())
    
    if user == 1:
        print(metodo_de_clase.Palindromo.esPalindromo("Os ó"))