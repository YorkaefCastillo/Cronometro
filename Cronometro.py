#Este es un proyecto donde se creo un cronometro de minutos
import time

#Bloque que adorna el titulo
ador,Titulo = "","cronometro"
print(f"{ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{ador.center(50,'*')}")

#Bloque donde pide la cantidad de minutos
Cantidad = input("Cuantos minutos para su temporizador: ")
def cronometro(t):
    while t:
        minutos,segundos = divmod(t,60)
        tiempo = f"{minutos}:{segundos}"
        print(tiempo,end="\r")
        time.sleep(1)
        t +=1
        if minutos == 2:
            print("Tiempo Finalizado")
            break
t = 1
cronometro(t)

