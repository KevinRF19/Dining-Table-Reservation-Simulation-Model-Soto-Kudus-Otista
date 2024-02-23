#Hari 7 (Minggu, 25 Juni 2023)
print("Model Solver Reservasi Meja Makan Soto Kudus Otista", end= "\n\n")
print("Minggu, 25 Juni 2023. Pukul 11.00 - 13.30", end= "\n\n")
print("Tamu ke-1, pukul 11.16 - 11.32", end= "\n\n") #tamu 1
c = 8
e = 12
f = 2
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 12:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f += 1

if c == 8 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,5,6,7", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-2, pukul 11.19 - 11.37", end= "\n\n") #tamu 2
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 3:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 3:
        break
    f += 1

if c == 3 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,4,5,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-3, pukul 11.28 - 11.56", end= "\n\n") #tamu 3
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 5:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 1:
        break
    f -= 1

if c == 5 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-4, pukul 11.40 - 11.51", end= "\n\n") #tamu 4
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 4:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 6:
        break
    f += 1

if c == 4 and e == 6 and f == 6:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-5, pukul 11.41 - 12.10", end= "\n\n") #tamu 5
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 6:
        
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 3:
        break
    f -= 1

if c == 6 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,5,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-6, pukul 11.52 - 12.10", end= "\n\n") #tamu 6
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 2:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f -= 1

if c == 2 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,3,4,5,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-7, pukul 11.57 - 12.15", end= "\n\n") #tamu 7
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 3:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f += 1

if c == 3 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,4,5,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-8, pukul 12.03 - 12.25", end= "\n\n") #tamu 8
#meja 4
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 4:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 4:
        break
    f += 1

if c == 4 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 5:
        break
    e += 1

if c == 4 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

if c == 4 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

#meja 5
while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 5:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

if c == 5 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 5:
        break
    e += 1

if c == 5 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

if c == 5 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-9, pukul 12.04 - 12.23", end= "\n\n") #tamu 9
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 4:
        break
    f += 1

if c == 8 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 5:
        break
    e += 1

if c == 8 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

if c == 8 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 7:
        break
    e += 1

if c == 8 and e == 7 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 8:
        break
    e += 1

if c == 8 and e == 8 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 9:
        break
    e += 1

if c == 8 and e == 9 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 10:
        break
    e += 1

if c == 8 and e == 10 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 11:
        break
    e += 1

if c == 8 and e == 11 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 12:
        break
    e += 1

if c == 8 and e == 12 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,6,7", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-10, pukul 12.08 - 12.27", end= "\n\n") #tamu 10
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 1:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 3:
        break
    f -= 1

if c == 1 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 2,3,4,5,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-11, pukul 12.14 - 12.41", end= "\n\n") #tamu 11
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 7:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f -= 1

if c == 7 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,5,6,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-12, pukul 12.16 - 12.43", end= "\n\n") #tamu 12
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 3:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f += 1

if c == 3 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,4,5,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-13, pukul 12.25 - 12.46", end= "\n\n") #tamu 13
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 4:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f += 1

if c == 4 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,5,6,7,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-14, pukul 12.33 - 12.37", end= "\n\n") #tamu 14
#meja 1
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 1:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 2:
        break
    f += 1

if c == 1 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

#meja 2
while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 2:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 3:
        break
    f += 1

if c == 2 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 5,6,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-15, pukul 12.41 - 13.03", end= "\n\n") #tamu 15
#meja 6
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 6:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 5:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 5:
        break
    f += 1

if c == 6 and e == 5 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

if c == 6 and e == 6 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

#meja 7
while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 7:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 4:
        break
    f -= 1

if c == 7 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 5:
        break
    e += 1

if c == 7 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

if c == 7 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,5,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-16, pukul 13.12 - 13.44", end= "\n\n") #tamu 16
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 7:
        break
    c += 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 6:
        break
    e += 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 1:
        break
    f -= 1

if c == 7 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,5,6,8", end= "\n\n\n")


print("Minggu, 25 Juni 2023")
print("Tamu ke-17, pukul 13.20 - 13.39", end= "\n\n") #tamu 17
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 1:
        break
    c -= 1

while e <= 50:
    print("E = " + str(e), end= "\n\n")
    if e == 4:
        break
    e -= 1

while f <= 50:
    print("F = " + str(f), end= "\n\n")
    if f == 3:
        break
    f += 1

if c == 1 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 2,3,4,5,6,8", end= "\n\n")