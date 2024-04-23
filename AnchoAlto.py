altura = int(input("Ingrese el alto del rectangulo  : "));
anchura = int(input("Ingrese el ancho del rectangulo: "));
print("");
def FormarRectangulo(alto,ancho):
    for i in range(0,alto):
        forma = "";
        j=0;
        for j in range(j,ancho,j+1):
            forma += "*";
        print(forma);
    print("");
FormarRectangulo(altura,anchura);