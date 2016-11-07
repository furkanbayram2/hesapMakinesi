
print("""
################################
#                              #
#     Şefik Furkan Bayram      #
#                              #
#   Toplama İçin 1'e Basınız   #
#   Çıkarma İçin 2'ye Basınız  #
#   Çarpma İçin 3'e Basınız    #
#   Bölme İçin 4'e Basınız     #
#                              #
################################
""")

while True:
    islemTipi=input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz: ")

    if(islemTipi=="1"):
        sayiBir = input("1. Sayıyı Giriniz: ")
        sayiIki = input("2. Sayıyı Giriniz: ")
        sonuc = int(sayiBir) + int(sayiIki)
        print("Sonuç: ",sonuc)

    elif(islemTipi=="2"):
        sayiBir = input("1. Sayıyı Giriniz: ")
        sayiIki = input("2. Sayıyı Giriniz: ")
        sonuc = int(sayiBir) - int(sayiIki)
        print("Sonuç: ", sonuc)

    elif (islemTipi=="3"):
        sayiBir = input("1. Sayıyı Giriniz: ")
        sayiIki = input("2. Sayıyı Giriniz: ")
        sonuc = int(sayiBir) * int(sayiIki)
        print("Sonuç: ", sonuc)

    elif (islemTipi=="4"):
        sayiBir = input("1. Sayıyı Giriniz: ")
        sayiIki = input("2. Sayıyı Giriniz: ")
        sonuc = int(sayiBir) / int(sayiIki)
        print("Sonuç: ", sonuc)

    else:
        print("Hatalı Bir Giriş Yaptınız !")


