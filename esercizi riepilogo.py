nome=input("come ti chiami?")
print(nome)
#prossimo ex
cognome= input("quale è il tuo cognome?")
#prossimo ex
nome_cognome= print(nome+" "+cognome)
#prossimo ex
print("il numero di caratteri totali è",len(str(nome))+len(str(cognome)))
#prossimo ex
frutta=("mela", "pera", "mango", "cocco")
print(frutta[3])

numeroA=input("scrivi un numero")
numeroB=input("scrivi un altro numero")
if numeroA<numeroB:
    print("il numero più piccolo è",numeroA,", ","quello più grande invece",numeroB)
else:
    print("il numero più piccolo è",numeroB,", ","quello più grande invece", numeroA)
colore = input('Inserisci il tuo colore:')
if colore == "rosso":
    print("bello")
elif colore == "ROSSO":
        print("bello")
else:
    print("brutto")
        
