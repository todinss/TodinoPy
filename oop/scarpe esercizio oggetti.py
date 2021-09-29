class scarpe:

    scarpe_negozio = 0

    #Metodo Costruttore
    def __init__(self, numero, marca, modello, colore, genere):

        self.numero = numero
        self.marca = marca
        self.modello = modello
        self.colore = colore 
        self.genere = genere

        scarpe.scarpe_negozio +=1
    
    def scheda_scarpe(self):
        return f'Scheda scarpe:\n numero:{self.numero}\n marca:{self.marca}\n modello:{self.modello}\n colore:{self.colore}\n genere:{self.genere}'
    
scarpa1 = scarpe(" 42 "," Nike "," Blazer "," Bianche "," Uomo")
print(scarpa1.scheda_scarpe())
