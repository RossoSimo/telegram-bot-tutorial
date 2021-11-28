# TUTORIAL GENERALE DI PYTHON 
## Input e Output
Qui riportiamo un esempio di input e output. Immettiamo il testo scelto dall'utente all'interno della variabile `string` e dopodichè la stampiamo concatenandola al nostro messaggio.
```python
string = input("inserisci una stringa ")
print("La stringa da te inserita é " + string)
```

## Tipi di variabili
Le variabili in python sono dinamiche, ovvero posso immagazzinare diversi tipi di dati (interi, strighe, floating point...) all'interno di una sola variabile.
```python
var1 = 1
print(type(var1))
print(var1)
var1 = 'ciao'
print(type(var1))
print(var1)
```

## Liste
Possiamo vedere le liste come delle specie di array, dove nelle varie "posizioni" andiamo a mettere una serie di variabili (se voglio anche di diverso tipo). Dove le varie "posizioni" vanno dallo 0 fino alla lunghezza della stringa meno 1.
```python
lista = ["Auricolari", 7, 12, "Gufo", 20.5]

print("Tutti gli elementi della lista:")
for i in lista:
    print(i)

print("\n3 elemento della lista:")
print(lista[2])

print(f"\nLunghezza della lista: {len(lista)}")
```

## Tuple
Qui vediamo una funzione che dati 2 valore come parametri ritorna una serie di dati elaborati. Come possiamo vedere non ritorna solo un dato come succede di solito, ma bensì 2. Quindi possiamo acquisire i dati ritornati della funzione con `var1, var2 = ...`
```python
def fun(var1, var2):
    return var1*2, var2

var1,var2 = fun(1, 'ciao' )
```

## Array e matrici
Dato che in python non ci sarebbero dei tipi array importiamo una libreria che ci permette di utilizzare questo tipo di struttura (con `numpy` possiamo fare solo array di interi). 
```python
import numpy as np

print("\nArray")
arrayNp = np.array([1, 2, 3, 5, 9])
print(arrayNp)
print(f"Il 3 elemento dell'array é {arrayNp[3]}")


print("\nMatrice")
matrixNp = np.matrix([[1, 7, 9],
                     [8, 4, 12]])
print(matrixNp)
print(type(matrixNp))

print(str(matrixNp))
print(type(str(matrixNp)))


print("\nSomma di Matrici")
matrix1 = np.matrix([[1, 7, 9],
                     [8, 4, 12]])
matrix2 = np.matrix([[12, 4, 2],
                     [7, 9, 2]])
print(f"Matrice 1 \n{matrix1}\n")
print(f"Matrice 1 \n{matrix2}\n")
print(f"La somma delle due matrici é: \n{matrix1+matrix2}")
```

## If, elif, else
```python
num = int(input("inserisci un valore "))
if num < 0 :
    print(f"Il numero {num} é minore di 0")
elif num >= 0 and num <= 10:
    print(f"Il numero {num} é compreso tra 0 e 10")
else:
    print(f"Il numero {num} é maggiore di 10")
```

## Cicli for e while
```python
import time

#-----------------FOR--------------------
print("Elementi presenti nella lista")
list = ["Marino","Giacomo","Anna","Marta","Luca"] #lista
for i in list: #per gli elementi presenti nella lista
    print(i)

#la funzione range() genere una sequenza di numeri da un inizio (se non esplicitato é 0) a una fine (sempre da esplicitare).
print("\nRange da 0 a 3")
for i in range(3):
    print(i)

print("\nRange da 3 a 9")
for i in range(3,9):
    print(i)

print("\nRange da 2 a 10 con intervalli di 2")
for i in range(2, 10, 2):
    print(i)

#-----------------WHILE--------------------

print("\nAttendo 10 secondi per continuare")
secondi = 1
while secondi <= 10:
    print(secondi)
    secondi+=1        #su python non esite num++
    time.sleep(1)

print("\nContinuo")
```

## Funzioni
Una funzione è una porzione di codice che può essere invocata da qualsiasi punto di un programma.
```python
def saluta(name):
    print(f'Ciao, {name}') 
    

if __name__ == "__main__":
    saluta("Luca")
    saluta("Anna")
```

## Variabili Globali
Una variabile globale è una variabile a cui puoi accedere in qualsiasi punto del programma.
```python
def saluta():
    print(f'Ciao, {nomeGlobale}') 

def cambiaNome():
    global nomeGlobale
    nomeGlobale = "Massimo"

if __name__ == "__main__":
    global nomeGlobale
    nomeGlobale = "Linda"
    saluta()
    cambiaNome()
    saluta()
```

## Set
Il metodo set serve per rimuovere i dupplicati e riordinare raccolte di dati.

```python
x = [1,2,190,2,3,4,5,5,79,5,9,9,9,7,7,7]
print("Lista x: " + str(x))
print("A seguire il set di x:" + str(set(x)))
```

## Dizionari
I dizionari sono elenchi di elementi ed ogni elemento dell'elenco corrisponde una chiave. Gli unici elementi che non possono essere messi all'internd di altri dizionari sono liste e dizionari
```python
dizionario = {"chiave":"valore"}

dizionario_dati_Sara = {"nome":"Sara", "eta":"22", "sesso":"F", "lavoro":"Insegnante"}
dizionario_dati_Marco = {"nome":"Marco", "eta":"19", "sesso":"M", "lavoro":"cuoco"}

print(f'etá di Sara: {dizionario_dati_Sara["eta"]}')            #La stringa ha una formattazione
print(f'Lavoro di Marco: {dizionario_dati_Marco["lavoro"]}')    #La stringa ha una formattazione
```

## Classi ed oggetti
Una classe, nella programmazione orientata agli oggetti, è un costrutto di un linguaggio di programmazione usato come modello per creare oggetti. Il modello comprende attributi e metodi che saranno condivisi da tutti gli oggetti creati (istanze) a partire dalla classe. Un oggetto è, di fatto, l'istanza di una classe.
```python
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def catInfo(self):
      print(f"Il gatto {self.name} di colore {self.color} ha {self.age} anni")


if __name__ == "__main__":
    Felix = Cat("Felix","6","Grigio")
    Felix.catInfo()

    Romeo = Cat("Romeo","3","Nero")
    Romeo.catInfo()

    Bianca = Cat("Bianca","2","Bianco")
    Bianca.catInfo()

```
