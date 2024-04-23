
numbers = [20,5,40,50,100];

def MaxMin(lista):

    if not lista:
        print("La lista está vacia");
        return None,None
    lista.sort();

    menor = lista[0];
    mayor = lista[-1];
    return menor,mayor;

menor,mayor = MaxMin(numbers);

print("lista: ",numbers)
print(f"El número mayor es: {mayor}, el número menor es: {menor}");