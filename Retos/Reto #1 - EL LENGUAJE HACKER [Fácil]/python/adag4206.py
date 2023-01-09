textOriginal=input("Ingrese caracter, palabra o frase a traducir ")
textOrigMayus=textOriginal.upper()
listaDividida=list(textOrigMayus)
listaOriginal=list(textOrigMayus)
tamañoLista=len(listaDividida)
listaTraducida=listaDividida
i=0
for i in range(tamañoLista):
    if listaDividida [i]=="A":
        listaTraducida[i]=4
    if listaDividida [i]=="B":
        listaTraducida[i]="I3"
    if listaDividida [i]=="C":
        listaTraducida[i]="["
    if listaDividida [i]=="D":
        listaTraducida[i]=")"
    if listaDividida [i]=="E":
        listaTraducida[i]=3
    if listaDividida [i]=="F":
        listaTraducida[i]="|="
    if listaDividida [i]=="G":
        listaTraducida[i]="&"
    if listaDividida [i]=="H":
        listaTraducida[i]="#"
    if listaDividida [i]=="I":
        listaTraducida[i]=1
    if listaDividida [i]=="J":
        listaTraducida[i]=",_|"
    if listaDividida [i]=="K":
        listaTraducida[i]=">|"
    if listaDividida [i]=="L":
        listaTraducida[i]=1
    if listaDividida [i]=="M":
        listaTraducida[i]="/\/\\"
    if listaDividida [i]=="N":
        listaTraducida[i]="^/"
    if listaDividida [i]=="O":
        listaTraducida[i]=0
    if listaDividida [i]=="P":
        listaTraducida[i]="|*"
    if listaDividida [i]=="Q":
        listaTraducida[i]="(_,)"
    if listaDividida [i]=="R":
        listaTraducida[i]="I2"
    if listaDividida [i]=="S":
        listaTraducida[i]=5
    if listaDividida [i]=="T":
        listaTraducida[i]=7
    if listaDividida [i]=="U":
        listaTraducida[i]="(_)"
    if listaDividida [i]=="V":
        listaTraducida[i]="\/"
    if listaDividida [i]=="W":
        listaTraducida[i]="\/\/"
    if listaDividida [i]=="X":
        listaTraducida[i]="><"
    if listaDividida [i]=="Y":
        listaTraducida[i]="j"
    if listaDividida [i]=="Z":
        listaTraducida[i]=2
print("El texto original ingresado es "+textOriginal)
print("El texto original ingresado letra por letra es ")
print(listaOriginal)
print("El texto traducido letra por letra es ")
print(listaTraducida)
print(*listaTraducida,sep='')