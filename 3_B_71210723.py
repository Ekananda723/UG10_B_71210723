#input
bil1 = float(input("Masukkan bilangan pertama: "))
bil2 = float(input("Masukkan bilangan kedua: "))
kalimat = input("Masukkan kalimat: ")

#kalkulasi
tambah = bil1+bil2
kurang = bil1-bil2
bagi = bil1/bil2
kali = bil1*bil2

#output
if "tambah" in kalimat:
    print("Hasil penjumlahan {} dengan {} adalah {}".format(bil1, bil2, tambah))
elif "kurang" in kalimat:
    print("Hasil pengurangan {} dengan {} adalah {}".format(bil1, bil2, kurang))
elif "bagi" in kalimat:
    print("Hasil pembagian {} dengan {} adalah {}".format(bil1, bil2, bagi))
elif "kali" in kalimat:
    print("Hasil perkalian {} dengan {} adalah {}".format(bil1, bil2, kali))
