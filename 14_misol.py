#Berilgan L metrni santimetr, millimetr, kilometrdagi qiymatlarni aniqlovchi dastur tuzing.
L = int(input("Metr kiriting: "))
sm = L * 100
mm = sm * 10
km = L / 1000
print(f"Berilgan {L} metr = {sm} santimetr = {mm} millimetr = {km} kilometr")