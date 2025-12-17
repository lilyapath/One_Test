import random 

elemen = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tanya = int(input("Tolong masukan panjang kata sandi! (Dalam angka)"))
password = "" #untuk menyimpan 

for i in range(tanya): 
    password += random.choice(elemen)
    
print("Ini adalah password Anda:", password)
