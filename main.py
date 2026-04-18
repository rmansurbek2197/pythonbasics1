sonlar = []
n = int(input("Sonlar sonini kiriting: "))
for i in range(n):
    son = float(input("Sonni kiriting: "))
    sonlar.append(son)
yigindi = sum(sonlar)
print("Sonlar yig'indisi:", yigindi)
print("Sonlar:")
for i, son in enumerate(sonlar, start=1):
    print(f"{i}. {son}")