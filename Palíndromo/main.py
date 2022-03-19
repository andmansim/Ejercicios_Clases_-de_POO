import metodo_de_clase
import metodo_de_instancia


if __name__=="__main__":
    print("¿Qué ejercicio quiere realizar, 1.Método de clase, 2.Método de instancia?" + " 1 / 2")
    user = int(input())
    
    if user == 1:
        print(metodo_de_clase.Palindromo.esPalindromo("Os ó"))
    elif user == 2:
        metodo_de_instancia.Palindromo("radar")
        print(metodo_de_instancia.Palindromo.test())

    else:
        print("Por favor elija entre 1 y 2")