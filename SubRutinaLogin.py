def Login(usuario,contraseña):
    intento=1;
    flag=0;
    while(flag == 0):
        if usuario != "admin" or contraseña != "admin123":
            print(f"Ingreso incorrecto intento: {intento}")
            usuario=input("Ingrese usuario: ");
            contraseña=input("Ingrese contraseña: ");
            intento = intento+1
        else:
            print("Ingreso correcto");
            flag = 1;

usuario    =input("Ingrese usuario: ");
contraseña =input("Ingrese contraseña: ");

Login(usuario,contraseña);