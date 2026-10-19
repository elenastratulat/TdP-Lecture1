import copy

from gestionale.core.prodotti import ProdottoRecord

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)] #oggetto che non ho bisogno di crearlo fuori, posso crearlo irettamente nella lista

print("Prodotti nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key= lambda x: x.prezzo_unitario, reverse=True)
print("Prodotti nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#calcolare prezzo totale carrello
tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#AGGIUNGERE
#aggiungere in coda
carrello.append(ProdottoRecord("Propdo", 100.0))
#aggiungere una lista
carrello.extend([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
#inserisce in una certa posizione un oggetto
carrello.insert(2, ProdottoRecord("ccc", 100.0))

#RIMUOVERE
carrello.pop()  #rimuove l'ultimo elemento
carrello.pop(2) #rimuove elemento in posizione 2
carrello.remove(p1)   #rimuove un elemento che so che esiste nella lista -> elimina il primo p1 che trova (non tutti)
#carrello.clear()  #elimina tutto ciò che c'è in lista

#SORTING
#carrello.sort() #ordinamento naturale degli oggetti inseriti in lista ---questo non funziona se gli oggetti contenuti non definiscono un metodo __lt__
#carrello.sort(reverse=True)  #ordina al contrario
#carrello.sort(key= function) #ordina in base a qualcosa che gli dico io

#creare una lista nuova ordinata in base alla lista di partenza
#carrello_ordinato = sorted(carrello)

carrello.reverse() #inverte l'ordine della lista
carrello_copia = carrello.copy()  # shallow copy -> crea una nuova lista che contiene gli stessi identici oggetti del carrello iniziale
carrello_copia2 = copy.deepcopy(carrello) #deep copy, ovvero copio anche il contenuto

#TUPLE
sede_principale = (45, 8) #latitudine e longitudine della sede di torino
sede_milano =(45, 9) #lat e long della sede di milano             sono immutabili le lat e le long
print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

#tupla di tuple
AliquotaIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquotaIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi =[p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tot, media, max, min =calcola_statistiche_carrello(carrello)

#tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"} #il secondo gold non lo calcola
print(categorie)
print(len(categorie))  #quanti elementi nel set
categorie2 ={"Platinum", "Elite", "Gold"}
categorie_all = categorie.union(categorie2)
categorie_union = categorie | categorie2  #simbolo unione
print(categorie_all)
print(categorie_union)

categorie_comuni = categorie & categorie2  #solo elementi comuni
print(categorie_comuni)

#solo elementi che stanno in uno dei due
categorie_esclusive= categorie - categorie2 #solo quelle di categorie che non sono contenute anche in categorie2
print(categorie_esclusive)

#differenza simmetrica
categorie_esclusive_simm = categorie ^ categorie2
print(categorie_esclusive_simm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                     ProdottoRecord("Mouse", 20.0),
                     ProdottoRecord("Tablet", 700.0)}
prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0),
                     ProdottoRecord("Mouse2", 20.0),
                     ProdottoRecord("Tablet2", 700.0)}
#metodi utili per set
s = set()
s1 = set()
prodotti_ordine_A.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiunge più elementi
s.remove(elem) #rimuove un elemento -> se l'elemento non esiste: KeyError
s.discard(elem) # rimuove un elemento senza arrabbiarsi se questo non esiste
s.pop() #rimuove e resistuisce un elemento
s.clear()

#operazioni di tipo insiemistico
s.union(s1) #s|s1 -> genera un set che unisce i due set di partenza
s.intersection(s1) #s&s1 -> solo elementi comuni
s.difference(s1) # s-s1 -> elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s^s1 -> elementi di s non contenuti in s1 e elementi di s1 non contenuti in s
s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) #se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) #se gli elementi di s e quelli di s1 sono diversi