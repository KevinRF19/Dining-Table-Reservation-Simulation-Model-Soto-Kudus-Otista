print("Senin, 19 Juni 2023. Pukul 11.00 - 13.30", end= "\n\n")
print("Tamu ke-1, pukul 10.56 - 11.09", end= "\n\n") #tamu 1
c = 8
e = 1
f = 8
s = 0

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 12:
    print("E = " + str(e), end= "\n\n")
    if e == 8:
        break
    e += 1

while f <= 12:
    print("F = " + str(f), end= "\n\n")
    if f == 8:
        break
    f += 1

if c == 8 and e == 8 and f == 8:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


c = 8
e = 1
f = 8

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 12:
    print("E = " + str(e), end= "\n\n")
    if e == 9:
        break
    e += 1

while f <= 12:
    print("F = " + str(f), end= "\n\n")
    if f == 8:
        break
    f += 1

if c == 8 and e == 9 and f == 8:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


c = 8
e = 1
f = 8

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 12:
    print("E = " + str(e), end= "\n\n")
    if e == 10:
        break
    e += 1

while f <= 12:
    print("F = " + str(f), end= "\n\n")
    if f == 8:
        break
    f += 1

if c == 8 and e == 10 and f == 8:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


c = 8
e = 1
f = 8

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 12:
    print("E = " + str(e), end= "\n\n")
    if e == 11:
        break
    e += 1

while f <= 12:
    print("F = " + str(f), end= "\n\n")
    if f == 8:
        break
    f += 1

if c == 8 and e == 11 and f == 8:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")


c = 8
e = 1
f = 8

while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 8:
        break
    c += 1

while e <= 12:
    print("E = " + str(e), end= "\n\n")
    if e == 12:
        break
    e += 1

while f <= 12:
    print("F = " + str(f), end= "\n\n")
    if f == 8:
        break
    f += 1

if c == 8 and e == 12 and f == 8:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
    s += 1
else:
    print("Solusi tidak ditemukan karena jumlah pengunjung tidak memenuhi constraint.", end= "\n\n")

print(f"Jumlah solusi yang ditemukan: {s}")
print("Nomor meja yang tersisa: 1,2,3,4,5,6,7", end= "\n\n\n")