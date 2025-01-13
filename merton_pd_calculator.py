import numpy as np
from scipy.stats import norm

# Données d'entrée
V = 1000  # Valeur actuelle des actifs
D = 800   # Dette à échéance
sigma = 0.2  # Volatilité des actifs (20%)
r = 0.05  # Taux sans risque (5%)
T = 1  # Temps jusqu'à l'échéance (1 an)

# Calcul de d1
d1 = (np.log(V / D) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

# Calcul de la Probabilité de Défaut (PD)
PD = 1 - norm.cdf(d1)

# Affichage du résultat
print(f"La probabilité de défaut (PD) est de {PD:.4f}")
