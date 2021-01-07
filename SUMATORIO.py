def suma(numero1, numero2):
    
    return numero1 + numero2;

numero1=int(input("Inserte un número \n"));
numero2=int(input("Inserte otro número \n"));

total=suma(numero1,numero2)
print(f"El resultado es {total}");


seguir=(input("¿Quiere seguir sumando? \n"));
while seguir!='No' or seguir!='no':
    numero1=total;
    numero2=int(input("Inserte otro número \n"));
    total=suma(numero1,numero2)
    print(f"El resultado es {total}");
    seguir=(input("¿Quiere seguir sumando? \n"));


