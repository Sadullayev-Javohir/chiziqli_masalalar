# 3ta son berilgan. Boshqa o'zgaruvchi ochmagan holda ularning qiymatini almashtiruvchi dastur tuzing.
a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))
c = int(input("Son kiriting: "))

a, b, c = b, c, a
print(f"a => {a}, b => {b}, c => {c}")