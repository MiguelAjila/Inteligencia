print ("Ducha Inteligente")
def DuchaElec():
    #Habtaciones es la variable donde se encuentra el entorno de la ducha
    Habitaciones = {'Sala': '0', 'Matrimonial': '0', 'Hospedaje': '0'}
    Habitacion = input("Habitacion donde de encuentra \nSala, Matrimonial, Hospedaje \n")
    Temperatura = float(input("Ingrese la temperatura del agua: "))
    #Como sabemos la temperatura es un elemento flotante.
    #Considerando el ambiente de Santo Domingo la temperatura normal es de 23 grados
    grados = 0.23

    DuchaElec()