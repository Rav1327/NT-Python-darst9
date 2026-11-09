import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="purple", s=100)
plt.title("O'qish vaqti va test bali")
plt.xlabel("Kunlik tayyorlanish vaqti (soat)")
plt.ylabel("Test bali")
plt.grid(True)
plt.show()

print("Izoh: O'qish vaqti oshgan sari test bali ham oshgan.")
print("Demak, ikki ko'rsatkich o'rtasida to'g'ri (musbat) bog'liqlik bor.")
