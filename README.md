Screet Notes – Şifreli Not Defteri

Screet Notes, Python ve Tkinter kullanılarak geliştirilmiş basit bir şifreli not defteri uygulamasıdır. Kullanıcılar notlarını başlık ve içerik ile kaydedebilir, bir şifre belirleyerek notlarını güvenli bir şekilde saklayabilir ve gerektiğinde şifreyi kullanarak notlarını çözebilir.

Özellikler

Notları başlık ve içerik ile kaydetme

Belirlediğiniz şifre ile notları AES tarzı basit bir şifreleme yöntemiyle koruma

Şifreyi kullanarak notları çözme

Basit ve kullanıcı dostu Tkinter arayüzü

Gereksinimler

Python 3.x

Ekstra kütüphane yok, Tkinter ve base64 standart Python kütüphaneleri ile çalışıyor.

Kullanım

Depoyu klonlayın veya indirin:

git clone <repository-url>


Screet Notes klasörüne gidin ve python <dosya_adı>.py ile çalıştırın:

python screet_notes.py


Açılan pencerede:

Başlık girin

Not girin

Şifre girin

Kaydet ve Şifrele butonuna tıklayın

Notları görmek veya çözmek için Çöz butonunu kullanın.

Notlar

Şifreleme basit bir karakter tabanlı şifreleme ve base64 kodlaması ile yapılmıştır. Profesyonel güvenlik için uygun değildir, eğitim ve öğrenim amaçlıdır.

Tüm notlar myscret.txt dosyasına kaydedilir.
