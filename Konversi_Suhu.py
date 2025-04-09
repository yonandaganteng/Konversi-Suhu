def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_ke_celcius(f):
    return (f - 32) * 5/9

print("=== Konversi Suhu ===")
print("1. Celcius ke Fahrenheit")
print("2. Fahrenheit ke Celcius")

pilihan = input("Pilih konversi (1/2): ")

if pilihan == '1':
    c = float(input("Masukkan suhu dalam Celcius: "))
    print("Hasil =", celcius_ke_fahrenheit(c), "F")
elif pilihan == '2':
    f = float(input("Masukkan suhu dalam Fahrenheit: "))
    print("Hasil =", fahrenheit_ke_celcius(f), "C")
else:
    print("Pilihan tidak valid!")
