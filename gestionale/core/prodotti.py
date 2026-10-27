
from dataclasses import dataclass

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

    def __str__(self):
        return f"{self.name} - disponibili: {self.quantity} pezzi a {self.price} $"

    def __repr__(self):
        return f"Prodotto(nome={self.name}, price={self.price}, quantity={self.quantity}, supplier={self.supplier})"

#questi due metodi str e repr non fanno altro che permetterci di rappresentare in stringa questo oggetti
#in due modi diversi --> repr più per il programmatore

    def __eq__(self, other: object):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)


    def __lt__(self, other: "Prodotto") -> bool :
        return self.price < other.price

    def prezzo_finale(self) -> float:
        return self.price*(1+self.aliquota_iva)

class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        #Prodotto.__init__()
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento
#in questo modo la classe è totalmente specificata e ha tutti i metodi e tutti gli attributi della classe Prodotto
    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto_percento/100)

class Servizio(Prodotto):
    def __init__(self, name:str, tariffa_oraria: float, ore: int):
        super().__init__(name=name, price=tariffa_oraria, quantity=1, supplier=None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore

class Abbonamento:
    def __init__(self, nome: str, prezzo_mensile: float, mesi: int):
        self.name = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self)-> float:
        return self.prezzo_mensile*self.mesi


MAX_QUANTITA = 1000

def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome, prezzo, quantity=1, supplier=None)

def _test_modulo():
    print("Sto testando il modulo prodotti.py")
    myproduct1 = Prodotto("Laptop", 1200.0, 12, "ABC")
    print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

    print(f"Il totale lordo di myproduct1 è: {myproduct1.valore_lordo()}")  #modo per chiamare un metodo di istanza (istanza.metodo)
    p3 = Prodotto.costruttore_con_quantità_uno("Auricolari", 200.0, "ABC") #modo per chiamare un metodo di classe (classe.metodo)
    print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}") #modo per chiamare metodo statico

    myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
    print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24
    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")

    p_a=Prodotto("Laptop", 1200.0, 12, "ABC")
    p_b = Prodotto("Mouse", 10, 14, "CDE")

    print("myproduct1 == p_a?", myproduct1 == p_a) #va a chiamare il metodo __eq__ appena implementato. Mi aspetto TRUE
    print("p_a == p_b?", p_a == p_b) #mi aspetto FALSE

    mylist=[p_a,p_b, myproduct1] #la lista l'ho creata nell'ordine: pc, mouse, pc ma quando vado a stamparla ordinata me la ordina in modo crescente
    mylist.sort()     #se la voglio ordinare al contrario scrivo mylist.sort(reverse=True) in ordine decrescente

    print("lista di prodotti ordinata")
    for p in mylist:
        print(f"- {p}")

if __name__ =="__main__":
    _test_modulo()

