
def calcularTemperatura():
    sumaDatos = 0;
    temperatura = 0;
    print("Programa para calcular la temperatura promedio durante 8 días");
    for i in range (0,8):
        print(f"Dia {i+1}\n")
        for y in range (0,20):
            datoIngresado = int(input(f"Ingrese la temperatura {y+1}: "));
            sumaDatos += datoIngresado;
    temperatura = (sumaDatos/8);
    print(f"La temperatura media de los 8 días fue de : {temperatura}°");


calcularTemperatura();