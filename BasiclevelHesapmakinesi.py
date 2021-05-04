print("""

HESAP MAKİNESİ
hangi işlemi yapmak istersiniz:
Toplama,Çıkarma,Bölme,Çarpma,
üssünü alma,Yüzde hesaplama
""")

islem = str(input("İşlem seçiniz: "))  # Burda kullanıcıdan hangi işlemi yapmak istediğini sorduk str() olarakda kısıtladık'ki 
                                       # bize sayı değeri giremesi girdiğinde hata alsın.

if islem == "Toplama":                      # burda girdiği değeri kontrol ettik ve eğer Toplama yazdıysa aşağıdaki işlemleri yaptırcaz
    sayi1 = int(input("sayi1 giriniz: "))   # burda bir değer daha istedik bu istediğimiz değer kullanıcının hangi toliycağı sayılardan biri olcak
    sayi2 = int(input("sayi2 giriniz: "))   # burda toplıycağı ikinci sayıyı istedik
    print("Sonuç:", sayi1 + sayi2)          # burda da kullanıcının verdiği değerleri işleme soktuk ve topladık.
elif islem == "TOPLAMA":                    # burda  kullanıcılar farklı yazabilceği için büyük yazdım kullanıcı büyük yazarsa hata almaması için.
    sayi1 = int(input("sayi1 giriniz: "))   # aynı işlemler diğerleriyle
    sayi2 = int(input("sayi2 giriniz: "))   # aynı işlemler 
    print("Sonuç:", sayi1 + sayi2)          # aynı işlemler
elif islem == "toplama":                    # burda da küçük yazdım hepsini kullanıcı küçük yazarsa hata almasın diye
    sayi1 = int(input("sayi1 giriniz: "))   
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 + sayi2)                               #BUNDAN SONRASI AYNI MANTIKLA İŞLEMLERİ DEVAM ETTİRDİM SADECE YAPTIĞI MATEMATİKSEL İŞLEMLER DEĞİŞİYOR
elif islem == "Çıkarma":                            
    sayi1 = int(input("sayi1 giriniz: "))                        # YANLIŞ BİR ŞEY YAZARSA NE OLCAĞINI GÖRMEK İÇİN KODUN EN ALTINA GİDİN
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif islem == "ÇIKARMA":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif islem == "çıkarma":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif islem == "Çarpma":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif islem == "ÇARPMA":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif islem == "çarpma":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif islem == "Bölme":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1/sayi2)
elif islem == "BÖLME":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1/sayi2)
elif islem == "bölme":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1/sayi2)
elif islem == "Üssünü alma":
    sayi1 = int(input("Taban sayısı girin:"))
    sayi2 = int(input("üs sayısı giriniz:"))
    print("Sonuç",sayi1**sayi2)
elif islem == "ÜSSÜNÜ ALMA":
    sayi1 = int(input("Taban saysı girin:"))
    sayi2 = int(input("Üs sayısı girin:"))
    print("Sonuç:",sayi1**sayi2)
elif islem == "üssünü alma":
    sayi1 = int(input("Taban saysı girin:"))
    sayi2 = int(input("Üs saysı girin:"))
    print("Sonuç",sayi1**sayi2)
elif islem == "Yüzde hesaplama":
    sayi1 = int(input("Yüzdesi hesaplancak sayı:"))
    sayi2 = int(input("Yüzde kaçını bulmak istiyorsunuz:"))
    print("sonuç:",(sayi1*sayi2)/100)
elif islem == "YÜZDE BULMA":
    sayi1 = int(input("Yüzdesi hesaplancak sayı:"))
    sayi2 = int(input("Yüzde kaçını bulmak istiyorsunuz:"))
    print("sonuç:",(sayi1*sayi2)/100)
elif islem == "yüzde bulma":
    sayi1 = int(input("Yüzdesi hesaplancak sayı:"))
    sayi2 = int(input("Yüzde kaçını bulmak istiyorsunuz:"))
    print("sonuç:",(sayi1*sayi2)/100)
else:                                                                  # BURDA KULLANICI YANLIŞ GİRERSE YAZIYOR YANİ ELSE.
    print("geçersiz işlem  yaptınız")                                   # KULLANICI YANLIŞ GİRDİĞİNDE GEÇERSİZ İŞLEM YAPTINIZ ÇIKTISI VERCEKTİR.