#scriviamo un codice python che modelli un semplice gestionale aziendale
#dovremo prevedere la possibilità di definire entità che modellano i prodotti, i clienti,
#offrire interfacce per calcolare i prezzi, eventualmente scontati, ...
from encodings import normalize_encoding


#prodotto1_nome = "Laptop"
#prodotto1_prezzo = 1200.0
#prodotto1_quantità = 5

#prodotto2_nome = "Mouse"
#prodotto2_prezzo = 12.0
#prodotto2_quantità = 15

#valore_magazzino = prodotto1_prezzo*prodotto1_quantità + prodotto2_prezzo*prodotto2_quantità
#print(f"Valore totale del mio magazzino:{valore_magazzino}")

#questo non è un bel codice: uno dei motivi è che io ho 7 variabili tutte scorrelate tra di loro, e mi devo
#ricordare della convenzione 1 (ad es per il prodotto 1) per sapere che le prime tre variabili sono parte
#di una stessa entità
#creiamo la stessa identica cosa ma con meno righe - CREIAMO UNA CLASSE

#in caso costruissimo una classe senza metterci dentro nulla
#class Prodotto:
#pass         -> pass è una keyword che noi mettiamo per evitare di farci dare errore in caso non scrivessimo nulla

class Prodotto:
    aliquota_iva = 0.22     #variabile di classe -> ovvero è la stessa per tutte le istante che verranno create
                                                #perchè appunto l'iva è uguale per tutti
    def __init__(self, name: str, price: float, quantity: int, supplier: str):               #def è un costruttore
        self.name = name                    #quando creo una proprietà, la devo anche assegnare
        self._price = None            #la assegno alle quantità che chi crea questo oggetto mi dice
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

#dopo il costruttore def bisogna definire alcuni parametri, parametri che dipendono dalle proprietà
#che vogliamo dare a quell'oggetto (in questo caso nome, prezzo, quantità come avevamo detto nel codice prima)

#nome, prezzo, quantità e supplier sono proprietà dell'istanza dell'oggetto, quindi le devo associare al self
#sto diecendo quindi che il self (quindi l'istanza che creo per la classe prodotto) avrà queste 4 proprietà

#posso anche trovare ad es supplier=None -> = si usa per dare un valore predefinito in caso l'utente non lo passi dall'esterno
#se quando creo l'istanza di questo oggetto Prodotto non mi viene passato un parametro supplier, automaticamente la mia
#classe assegna quel supplier al None

    def valore_netto(self):
        return self.price*self.quantity     #return è la keyword che mi consente di restituire all'esterno di un metodo una certa quantità

    def valore_lordo(self):
        netto = self.valore_netto()   #ho richiamato in questo metodo, un altro metodo della stessa classe grazie al fatto che mi passo il riferimento del self
        lordo = netto*(1+self.aliquota_iva)
        return lordo

#posso creare variabili di classe e posso creare anche metodi di classe (ovvero che non sono associate alla singola istanza ma sono
#valide per tutti) -> utilizzando i decoratori, che si introducono con @ e viene messo prima di un metodo, stando ad indicare
# che quel metodo è un metodo di classe e non un metodo di istanza -> è un metodo che creo una volta sola
    #lo faremo molto spesso per creare delle classi che implementano un pattern di programmazione
#i metodi di classe non prendono come input il self ma il cls perchè non sono un metodo dell'istanza self ma della classe e poi funzionano come
    #tutti gli altri costruttori

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        cls(name, price, 1, supplier)           #richiama l'init ma mi maschera un parametro, che in questo caso è un costruttore alternativo

#ci sono poi anche i metodi statici -> sono metodi non associati alla singola istanza, ma che sono di appoggio/supporto
    #essendo un metodo statico non devo passare ne self ne cls

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

#property anche lui si introduce come un decoratore con @, e vuol dire che cambiamo il contenuto sematico di quella funzione
#noi lo associamo alla variabile di cui noi vogliamo creare il getter and setter
    @property
    def price(self):  #equivalente a getter
        return self._price
#questa cosa ha senso quando io voglio fare dei controlli
    @price.setter   #solo ed esclusivamente se ho definito prima un getter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione, il prezzo non può essere negativo.")
        self._price = valore

myproduct1 = Prodotto("Laptop", 1200.0, 12, "ABC")
print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

print(f"Il totale lordo di myproduct1 è: {myproduct1.valore_lordo()}")  #modo per chiamare un metodo di istanza (istanza.metodo)
p3 = Prodotto.costruttore_con_quantità_uno("Auricolari", 200.0, "ABC") #modo per chiamare un metodo di classe (classe.metodo)
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}") #modo per chiamare metodo statico

myproduct2 = Prodotto("Mouse", 12.0, 15, "DEF")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")


#scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold","Silver","Bronze")
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione" che deve restituire una stringa formattata
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

class Cliente:
    def __init__(self, name: str, email: str, categoria: str):
        self.name = name
        self.email = email
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria
#questo setter verifica che questa categoria sia una delle tre se non lo è fa qualcosa, se lo è lo setta


    def descrizione(self):
        #"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.name} ({self.categoria}) - {self.email}"

cliente1 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
print(cliente1.descrizione())
cliente2 = Cliente("Mario Rossi", "mario.rossi@polito.it", "Silver" )
print(cliente2.descrizione())


#QUINDI ALL'INTERNO DI UNA CLASSE POSSO DEFINIRE 3 TIPI DI METODI:
#1. METODI DI ISTANZA (normali): definiti con il self
#2. METODI STATICI: che non sono associati a nessuna istanza e quindi non gli passo il self
#3. METODI DI CLASSE: che non si riferiscono alla singola istanza ma all'intera classe, definiti con il cls

#si modifichi la classe cliente in maniera tale che la proprietà categoria sia "protetta" e
#accetti solo ("gold", "silver", "bronze")