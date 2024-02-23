#model solver meja 1

#inisialisasi variabel yang dibutuhkan
c = 1
e = 1
f = 1

#pengkondisian mencari solver meja 1
while c <= 8:
    print("C = " + str(c), end= "\n\n")
    if c == 1:
        break
    c += 1

while e <= 4:
    if e == 4:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

while f <= 4:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 1 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")


#model solver meja 2

#pengkondisian mencari solver meja 2
while c <= 8:
    if c == 2:
        print("C = " + str(c), end= "\n\n")
        break
    c += 1

if c == 2 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")


#model solver meja 3

#pengkondisian mencari solver meja 3
#(nilai variabel tertentu dilakukan looping pengurangan untuk mencari solusi berikutnya)
while c <= 8:
    if c == 3:
        print("C = " + str(c), end= "\n\n")
        break
    c += 1

if c == 3 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 5:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

if c == 3 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 3 and e == 5 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 6:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 3 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 3 and e == 6 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 6:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 3 and e == 6 and f == 6:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")


#model solver meja 4

#pengkondisian mencari solver meja 4
#(nilai variabel tertentu dilakukan looping pengurangan untuk mencari solusi berikutnya)
while c <= 8:
    if c == 4:
        print("C = " + str(c), end= "\n\n")
        break
    c += 1

while e <= 6:
    if e == 4:
        print("E = " + str(e), end= "\n\n")
        break
    e -= 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 4 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 5:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

if c == 4 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 4 and e == 5 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 6:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 4 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 4 and e == 6 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 6:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 4 and e == 6 and f == 6:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")


#model solver meja 5

#pengkondisian mencari solver meja 5
#(nilai variabel tertentu dilakukan looping pengurangan untuk mencari solusi berikutnya)
while c <= 8:
    if c == 5:
        print("C = " + str(c), end= "\n\n")
        break
    c += 1

while e <= 6:
    if e == 4:
        print("E = " + str(e), end= "\n\n")
        break
    e -= 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 5 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 5:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

if c == 5 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 5 and e == 5 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 6:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 5 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 5 and e == 6 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 6:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 5 and e == 6 and f == 6:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")


#model solver meja 6

#pengkondisian mencari solver meja 6
#(nilai variabel tertentu dilakukan looping pengurangan untuk mencari solusi berikutnya)
while c <= 8:
    if c == 6:
        print("C = " + str(c), end= "\n\n")
        break
    c += 1

while e <= 6:
    if e == 4:
        print("E = " + str(e), end= "\n\n")
        break
    e -= 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 6 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 5:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

if c == 6 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 6 and e == 5 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 6:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 6 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 6 and e == 6 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 6:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 6 and e == 6 and f == 6:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")


#model solver meja 7

#pengkondisian mencari solver meja 7
#(nilai variabel tertentu dilakukan looping pengurangan untuk mencari solusi berikutnya)
while c <= 8:
    if c == 7:
        print("C = " + str(c), end= "\n\n")
        break
    c += 1

while e <= 6:
    if e == 4:
        print("E = " + str(e), end= "\n\n")
        break
    e -= 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 7 and e == 4 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 5:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

if c == 7 and e == 5 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 7 and e == 5 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while e <= 6:
    if e == 6:
        print("E = " + str(e), end= "\n\n")
        break
    e += 1

while f <= 6:
    if f == 4:
        print("F = " + str(f), end= "\n\n")
        break
    f -= 1

if c == 7 and e == 6 and f == 4:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 5:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 7 and e == 6 and f == 5:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")

while f <= 6:
    if f == 6:
        print("F = " + str(f), end= "\n\n")
        break
    f += 1

if c == 7 and e == 6 and f == 6:
    print(f"Solusinya adalah: C = {c}, E = {e}, F = {f}", end= "\n\n")
else:
    print("Solusi tidak ditemukan.")