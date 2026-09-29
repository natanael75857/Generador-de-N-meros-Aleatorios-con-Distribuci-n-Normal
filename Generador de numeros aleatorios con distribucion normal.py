modulo = 10000
a = 41
c = 17
z0 = 12345

#Función que genera el número aleatorio basado en la semilla z0 y los parámetros establecidos
def Generador(): 
    global z0
    z0 = (z0 * a + c) % modulo
    Uniforme = z0/ modulo
    return Uniforme

#Entrada del usuario para los parametros en la distribución normal
media = float(input("Ingresa la media: "))
varianza = float(input("Ingrese la varianza: "))
n = int(input("Ingrese la cantidad números a generar: "))

#La raíz cuadrada de cualquier número, es el número elevado a 1/2
sigma = varianza**0.5 

#Ciclo For que evalúa cada número del generador en el rango de datos establecidos por "n"
for i in range(n):
    SumaUniforme = 0
    for j in range(30):
        Uniforme = Generador()
        SumaUniforme += Uniforme
    NumNormal = SumaUniforme - 15

    X = NumNormal*sigma + media

    print("Valor ", i+1, ":", X)

    input("\nPresiona Enter para finalizar el programa...")