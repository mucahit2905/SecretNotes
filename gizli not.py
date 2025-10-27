import tkinter
from tkinter import *
from tkinter import messagebox
import base64


# Şifreleme
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

# kaydetme
def kaydet():

    baslik=baslik_text.get(1.0,END)
    yazi=not_text.get(1.0,END)
    sifre=sifre_text.get(1.0,END)

    if len(baslik)== 0 or len(yazi)== 0 or len(sifre)==0:
        messagebox.showinfo(title="Hata", message="Bütün bilgileri giriniz !!!")

    else:
        mesage_encrypted=encode(sifre, yazi)
        try:
            with open("myscret.txt","a",encoding="utf-8")as data_file:
                 data_file.write(f"{baslik}\n{mesage_encrypted}")

        except FileNotFoundError:
            with open("myscret.txt","w",encoding="utf-8")as data_file:
                data_file.write(f"{baslik}\n{mesage_encrypted}")

        finally:
            baslik_text.delete(1.0,END)
            sifre_text.delete(1.0,END)
            not_text.delete(1.0,END)

# şifreyi çözme
def decrypt_notes():
    message_encrypted = not_text.get("1.0", END)
    master_secret = sifre_text.get("1.0", END)

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Hata", message="Lütfen tüm bilgileri giriniz.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            not_text.delete("1.0", END)
            not_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Hata", message="Lütfen bilgilerin şifreli olduğundan emin olun.")


window=Tk()
window.geometry("600x650")
window.title("Screet Notes")

resim=tkinter.PhotoImage(file="logo.png")

kucuk_resim=resim.subsample(8,9)
logo=Label(window,image=kucuk_resim)
logo.pack(pady=5)


baslik_label=Label(text="Başlık giriniz")
baslik_label.pack(pady=5)

baslik_text=Text(width=30,height=1)
baslik_text.pack(pady=5)

not_label=Label(text="Not giriniz")
not_label.pack(pady=5)

not_text=Text(width=40,height=20)
not_text.pack(pady=5)

sifre_label=Label(text="Sifre giriniz")
sifre_label.pack(pady=5)

sifre_text=Text(width=30,height=1)
sifre_text.pack(pady=5)

sifrele_buton=Button(width=25 ,height=1,text="Kaydet ve Şifrele", command=kaydet)
sifrele_buton.pack(pady=5)

kaydet_buton=Button(width=20 ,height=1,text="Çöz" ,command=decrypt_notes)
kaydet_buton.pack(pady=5)
window.mainloop()