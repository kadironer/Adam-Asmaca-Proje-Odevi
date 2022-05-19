import random
def oyun():

    kelimeler = random.choice(["terminator" , "avengers" , "matrix" , "tenet" , "jumanji" , "shazam" , "lucy" , "deadpool" , "kingsman" , "transformers" ])
    gecerliHarfler = 'abcdefghijklmnopqrstuvwxyz'
    toplamHak = 10
    yapilanTahmin = ''
    print("Filmin adını bulabilmek için 10 hakkınız var")
    while len(kelimeler) > 0:
        asilKelime = ""
        hataliTahminSayisi = 0

        for harf in kelimeler:
            if harf in yapilanTahmin:
                asilKelime = asilKelime + harf
            else:
                asilKelime = asilKelime + "_" + " "
        if asilKelime == kelimeler:
            print(asilKelime)
            print("Tebrikler kazandınız")
            break

        print("Filmin adını tahmin edin:" , asilKelime)
        tahmin = input()

        if tahmin in gecerliHarfler:
            yapilanTahmin = yapilanTahmin + tahmin
        else:
            print("girdiğiniz harfi kontrol edin")
            tahmin = input()

        if tahmin not in kelimeler:
            toplamHak = toplamHak - 1
            if toplamHak == 9:
                print("9 hakkınız kaldı")
                print("  --------  ")
            if toplamHak == 8:
                print("8 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
            if toplamHak == 7:
                print("7 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if toplamHak == 6:
                print("6 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if toplamHak == 5:
                print("5 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 4:
                print("4 hakkınız kaldı")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 3:
                print("3 hakkınız kaldı")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 2:
                print("2 hakkınız kaldı")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 1:
                print("1 hakkınız kaldı")
                print("Dikkatli kullanın")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 0:
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")

                print("Oyun bitti")
                print("bilemediniz ve kaybettiniz")
                break


oyun()