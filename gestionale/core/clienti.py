#scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold","Silver","Bronze")
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione" che deve restituire una stringa formattata
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

from dataclasses import dataclass

categorie_valide = {"Gold", "Silver", "Bronze"}

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
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria
#questo setter verifica che questa categoria sia una delle tre se non lo è fa qualcosa, se lo è lo setta


    def descrizione(self):
        #"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.name} ({self.categoria}) - {self.email}"

@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

    def __str__(self):
        return f"{self.name} -- {self.email} ({self.categoria})"

def _test_modulo():
    cliente1 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
    print(cliente1.descrizione())
    cliente2 = Cliente("Mario Rossi", "mario.rossi@polito.it", "Silver" )
    print(cliente2.descrizione())

if __name__ == "__main__":
    _test_modulo()