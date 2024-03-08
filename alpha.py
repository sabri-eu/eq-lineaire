from math import ceil

alpha = float(input("Valeur de alpha : "))
a = int(input("Valeur de a : "))
b = int(input("Valeur de b : "))
c = int(input("Valeur de c : "))
d = int(input("Valeur de d : "))

e = a - b * alpha
f = c - d * alpha
print("e =", e, "f =", f)

prems = -f / e
deus = -d / b
print("prems =", prems, "deus =", deus)

signe = input("Signe recherché (>, <) : ")

print("Écrire sur le cahier :")
print("------------------------------------")
print("a =", ceil(e), "| b =", ceil(f))
print("-b/a =", ceil(prems), "| x = -", d, "/", b, "=", ceil(deus))

if prems > deus:
    print("x en premier")
else:
    print("-b/a en premier")

if e > 0:
    print("a positif")
else:
    print("a négatif")

if deus > 0:
    print("x négatif")
else:
    print("x positif")

if prems > 0:
    if prems == deus:
        print("S = Flemme")
    elif prems > deus:
        if signe == ">":
            print("S =", "[" + str(-d) + "/" + str(b) + "; -b/a]")
        elif signe == "<":
            print("S =", "]-∞;" + str(-d) + "/" + str(b) + "[ U [-b/a; +∞[")
    elif deus > prems:
        if signe == ">":
            print("S =", "[-b/a; " + str(-d) + "/" + str(b) + "[")
        elif signe == "<":
            print("S =", "]-∞;-b/a] U ]" + str(-d) + "/" + str(b) + "; +∞[")

if prems < 0:
    if prems == deus:
        print("S = Flemme")
    elif prems > deus:
        if signe == "<":
            print("S =", "[" + str(-d) + "/" + str(b) + "; -b/a]")
        elif signe == ">":
            print("S =", "]-∞;" + str(-d) + "/" + str(b) + "[ U [-b/a; +∞[")
    elif deus > prems:
        if signe == "<":
            print("S =", "[-b/a; " + str(-d) + "/" + str(b) + "[")
        elif signe == ">":
            print("S =", "]-∞;-b/a] U ]" + str(-d) + "/" + str(b) + "; +∞[")
