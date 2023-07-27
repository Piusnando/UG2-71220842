def volumetabung(d,t):
    vtabung=22/7*d*t
    return vtabung
def volumekubus(s):
    vkubus=s**3
    return vkubus
def volumebalok(p,l,t):
    vbalok=p*l*t
    return vbalok

print("==================== KALKULATOR CERDAS ====================")
print("Pilihlah bangun yang ingin anda hitung(inputan angka saja) :")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")
pilih=int(input(">> "))
if pilih==1:
    d=int(input("Masukan diameter(cm) : "))
    t=int(input("Masukan tinggi(cm) : "))
    print("Volume tabung adalah ",volumetabung(d,t),"cm")
elif pilih==2:
    s=int(input("Masukan sisi(cm) : "))
    print("Volume kubus adalah ",volumekubus(s),"cm")
elif pilih==3:
    p=int(input("Masukan panjang(cm) : "))
    l=int(input("Masukan lebar(cm) : "))
    t=int(input("Masukan tinggi(cm) : "))
    print("Volume balok adalah ",volumebalok(p,l,t),"cm")
else:
    print("Inputan yang anda masukan salah !!")