import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

eng_kop_son = max(sotuv)
eng_kam_son = min(sotuv)
eng_kop_mahsulot = mahsulotlar[sotuv.index(eng_kop_son)]
eng_kam_mahsulot = mahsulotlar[sotuv.index(eng_kam_son)]

print("Eng ko'p sotilgan mahsulot:", eng_kop_mahsulot, eng_kop_son)
print("Eng kam sotilgan mahsulot:", eng_kam_mahsulot, eng_kam_son)

plt.bar(mahsulotlar, sotuv, color="orange")
plt.title("Bir haftalik savdo")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan soni")
plt.show()
