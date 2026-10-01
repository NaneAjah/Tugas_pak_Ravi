def tambah(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

a = int(input("Masukan Angka Pertama : "))
b = int(input("Masukan Angka Kedua : "))

print(f"{a} + {b} = {tambah(a, b)}")
print(f"{a} - {b} = {pengurangan(a, b)}")
print(f"{a} * {b} = {kali(a, b)}")
print(f"{a} / {b} = {bagi(a, b)}")

#version 2.0