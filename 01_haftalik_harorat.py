import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
harorat = [18, 20, 17, 23, 25, 22, 27]

plt.plot(kunlar, harorat, marker="o")
plt.title("Haftalik harorat")
plt.xlabel("Kunlar")
plt.ylabel("Harorat (°C)")
plt.grid(True)
plt.show()
