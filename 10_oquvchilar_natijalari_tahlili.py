import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = round(sum(ballar) / len(ballar), 2)

print("Eng yuqori ball:", ismlar[ballar.index(eng_yuqori)], eng_yuqori)
print("Eng past ball:", ismlar[ballar.index(eng_past)], eng_past)
print("O'rtacha ball:", ortacha)

print("Xulosa 1: Eng yuqori natijani Aziza (95), eng pastini Sardor (65) ko'rsatdi.")
print("Xulosa 2: O'rtacha ball 81.83, 3 ta o'quvchi (Vali, Malika, Aziza) o'rtachadan yuqori.")
print("Xulosa 3: Eng yuqori va eng past ball farqi 30 ball, shuning uchun past natijalilarga qo'shimcha yordam kerak.")

plt.bar(ismlar, ballar, color="skyblue")
plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ball")
plt.grid(True)
plt.savefig("oquvchilar_natijasi.png")
plt.show()
