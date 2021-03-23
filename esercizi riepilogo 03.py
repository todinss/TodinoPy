Mario = {"matematica" : 6, "italiano" : 6, "scienze" : 7, "inglese" : 4}
Giovanni ={"matematica" : 4, "italiano" : 6, "scienze" : 5, "inglese" : 7}
Paola ={"matematica" : 9, "italiano" : 6, "scienze" : 8, "inglese" : 8}
a =sum(Mario.values())
b =sum(Giovanni.values())
c =sum(Paola.values())
print("la maedia di Mario è", a/4)
print("la maedia di Giovanni è", b/4)
print("la maedia di Paola è", c/4)


#oppure 

import statistics
 
Media_Mario=statistics.mean(Mario)

