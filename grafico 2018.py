print("vuoi visualizzare il grafico dell 2018? se si premi invio")
input()
import numpy as np
import matplotlib.pyplot as plt

x = np.array([43.3, 28.7, 21.3, 4.5, 2.1 ])
label = ["non lo usano", "tutti i giorni", "uno più volte alla settimana", "qualche volta al mese", "qualche volta all'anno"]

plt.pie(x, labels=label)
plt.show()
