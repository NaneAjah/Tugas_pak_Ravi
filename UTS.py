def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

a = int(input("Masukan Angka Pertama : "))
b = int(input("Kedua : "))

print(f"{a} + {b} = {tambah(a, b)}")
print(f"{a} - {b} = {kurang(a, b)}")
print(f"{a} * {b} = {kali(a, b)}")
print(f"{a} / {b} = {bagi(a, b)}")

# update 1.0{nizar}