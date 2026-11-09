import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(mashgulot, masofa, color="green", marker="s", linewidth=3)
plt.title("Sportchining yugurgan masofasi")
plt.xlabel("Mashg'ulot")
plt.ylabel("Masofa (km)")
plt.grid(True, linestyle="--")
plt.show()

print("Izoh: Masofa 2.0 km dan 4.0 km gacha o'sdi, ya'ni natija ikki barobar oshdi.")
print("Faqat 3-mashg'ulotda masofa biroz kamaydi, qolgan mashg'ulotlarda doimiy o'sish kuzatildi.")
