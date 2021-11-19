#input
angka = int(input("Masukkan angka: "))

#output
if angka%2 == 0 and angka%3 >= 1:
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: YA")
else: exit(print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan"))

print()

if angka%5 == 0 or angka%10 == 0:
    print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
else: print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")
