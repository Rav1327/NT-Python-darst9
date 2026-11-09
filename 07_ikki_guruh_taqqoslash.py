import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="blue", marker="o", label="A guruh")
plt.plot(testlar, guruh_b, color="red", marker="s", label="B guruh")
plt.title("Ikki guruh test natijalari")
plt.xlabel("Testlar")
plt.ylabel("Ball")
plt.legend()
plt.grid(True)
plt.show()

yigindi_a = sum(guruh_a)
yigindi_b = sum(guruh_b)
print("A guruh o'rtacha bali:", yigindi_a / len(guruh_a))
print("B guruh o'rtacha bali:", yigindi_b / len(guruh_b))
print("Izoh: B guruh o'rtacha natijasi yuqori, oxirgi testlarda ham oldinda.")
print("A guruh esa barqaror o'sdi, B guruhda esa o'zgarish kuchliroq bo'ldi.")
