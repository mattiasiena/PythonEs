#Codice che comprende tutti gli esercizi 
#Importare la libreria Math per eventuali funzioni (Pi greco, SQRT)
import math
#Assegnamo a numEs un valore esterno al range (1-7)
numEs=8

#Ciclo creato per non scegliere esercizi fuori dal range (1-7)
#Scegli tramite questo input quale esercizio svolgere
while numEs>1 and numEs>7:
    numEs=int(input("Scegli quale esercizio fare (da 1 a 7): "))
    #Controllo dell'esercizio scelto
    if numEs>=1 and numEs<=7: 
        print("Hai scelto l'esercizio ", numEs, "\n")
    else:
        print("L'esercizio non esiste.")
    
if numEs==1:
    #Calcola il quadrato di un numero fornito da tastiera
    #Input della variabile Num1
    num1=int(input("Inserisci il valore: "))
    #Calcolaliamo il quadrato della variabile
    quad1=num1**2
    #Stampiamo il valore calcolato
    print(quad1)
    
elif numEs==2:
    #Data la diagonale, calcola il perimetro e l'area di un quadrato
    #Input del valore della diagonale
    diagonale2=int(input("Inserisci il valore: "))
    #Calcoliamo l'area tramite la diagonale
    area2=(diagonale2**2)/2
    #Calcoliamo il perimetro tramite la diagonale
    perimetro2=4*(math.sqrt(area2))
    #Stampiamo il valore dell'area e del perimetro
    print("Valore dell'area: ", area2, ", valore del perimetro: ", perimetro2)
    
elif numEs==3:
    #Data la misura della circonferanza, calcola l'area del cerchio
    #Input del valore della circonferenza
    circonferenza3=int(input("Inserire il valore: "))
    #Constante creata per il calcolo dell'area
    const3=4*math.pi
    #Calcolare l'area
    area3=(circonferenza3**2)/const3
    #Stampiamo il valore dell'area
    print("Il valore dell'area è: ", area3)
    
elif numEs==4:
    #Calcola la misura della diagonale di un rettangolo, note le sue dimensioni
    #Input del valore della base e dell'altezza
    base4=int(input("Inserire il valore della base: "))
    altezza4=int(input("Inserire il valore dell'altezza: "))
    #Calcolo della diagonale
    diagonale4=math.sqrt((base4**2)+(altezza4**2))
    #Output della diagonale
    print("Il valore della diagonale è: ", diagonale4)
    
elif numEs==5:
    #Calcola il volume di un cubo, nota la lunghezza di uno spigolo
    #Input del valore del lato=spigolo
    lato5=int(input("Valore del lato: "))
    #Calcolo del volume
    volume5=lato5**3
    #Output del valore del volume
    print("Il valore del volume è: ", volume5)
    
elif numEs==6:
    #Dato il lato, trova il perimetro e l'area di un esagono regolare
    #Input del valore del lato
    lato6=int(input("Inserire il valore del lato: "))
    #Calcolo dell'area e del perimetro
    perimetro6=lato6*6
    area6=(lato6**2)*2,598
    #Stampa del valore dell'area e del perimetro
    print("Valore dell'area: ", area6, ", valore del perimetro: ", perimetro6)
    
elif numEs==7:
    #Dati i voti di 3 prove di uno studente, calcola la media dei voti
    #Input dei voti delle tre prove
    prova1=int(input("Voto della prima prova: "))
    prova2=int(input("Voto della seconda prova: "))
    prova3=int(input("Voto della terza prova: "))
    #Calcolo della somma
    somma7=prova1+prova2+prova3
    #Calcolo della media dei 3 voti
    media7=somma7/3
    print("Il valore della media è: ", media7)

