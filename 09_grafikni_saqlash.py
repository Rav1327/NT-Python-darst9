import matplotlib.pyplot as plt

oylar = [1, 2, 3, 4, 5, 6, 7, 8]
kitoblar = [2, 3, 1, 4, 5, 3, 6, 7]

plt.plot(oylar, kitoblar, color="teal", marker="o")
plt.title("Oylik o'qilgan kitoblar soni")
plt.xlabel("Oylar")
plt.ylabel("Kitoblar soni")
plt.grid(True)
plt.savefig("natija.png")
plt.show()
