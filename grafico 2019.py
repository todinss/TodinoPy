print("vuoi visualizzare il grafico dell 2019 ? se si premi invio")
input()
import numpy as np
import matplotlib.pyplot as plt

x = np.array([43.2, 28.5, 20.6, 5.3, 2.5 ])
label = ["non lo usano", "tutti i giorni", "uno più volte alla settimana", "qualche volta al mese", "qualche volta all'anno"]

plt.pie(x, labels=label)
plt.show()

