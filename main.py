from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdinecConSconto

print("===========================================================")

p1=Prodotto("Ebook Reader", 120.0, 1 , "AAA")
p2=crea_prodotto_standard("Tablet", 750)

print(p1)
print(p2)

#MODI PER IMPORTARE
#1. from prodotti import ProdottoScontato
#p21=ProdottoScontato("Auricolari", 230, 1, "ABC", 10)

#2. from prodotti import ProdottoScontato as ps   #ps serve per rinominare l'oggetto che riporto
#p3=ps("Auricolari", 230, 1, "ABC", 10)

#3. import prodotti
#p4 = prodotti.ProdottoScontato("Auricolari", 230, 1, "ABC", 10)

#4.import prodotti as p
#p5 = p.ProdottoScontato("Auricolari", 230, 1, "ABC", 10)

print("===========================================================")

c1=Cliente("Mario Rossi","mail@mail.com", "Gold")

cliente1=ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1=ProdottoRecord("Laptop", 1200.0)
p2=ProdottoRecord("Mouse", 20)

ordine=Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
ordine_scontato=OrdinecConSconto([RigaOrdine(p1,2), RigaOrdine(p2, 10)], cliente1, 0.1)

print(ordine)
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto: ", ordine_scontato.totale_netto())
print("Totale lordo scontato: ", ordine_scontato.totale_lordo(0.22))

#totale netto esiste in OrdineConSconto
#totale lordo non esiste in OrdineConSconto ma esiste in Ordine -> il mio codice va a vedere se in OrdineConSconto
#ho definito totale lordo, non l'ho definito quindi va a richiamare l'implementazione della sua pre classe

print("----------------------------------------------------------------------")

#nel package gestionale scriviamo un modulo fatture.py che contenga:
#-una classe Fattura che contiene un Ordine, un numero fattura e una data
#-un metodo genera_fattura() che restituisce una stringa formattata con tutte le info della fattura