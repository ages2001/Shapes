def main():
    print("Number 1: ", end="")
    number1 = tamsayi_al(2, 10)

    print("Number 2: ", end="")
    number2 = tamsayi_al(2, 10)

    print("Number 3: ", end="")
    number3 = tamsayi_al(2, 10)

    print("Character 1: ", end="")
    character1 = cizim_karakteri_al()

    print("Character 2: ", end="")
    character2 = cizim_karakteri_al()

    print()
    dikdortgen_ciz(number1, number2 + number3, character1)
    print()
    kare_ciz(number3, character2)
    print()
    ikizkenar_ucgen_ciz(number2, character1)
    print()
    ters_ikizkenar_ucgen_ciz(number3, character2)
    print()
    sag_dik_ucgen_ciz(number3, character1)  # bonus
    print()
    ters_dik_ucgen_ciz(number3, character2)  # bonus
    print()
    yan_dik_ucgen_ciz(2 * number1 - 1, character1, character2)
    print()
    eskenar_dortgen_ciz(2 * number1 + 1, character1)
    print()
    kum_saati_ciz(2 * number3, character1, character2)
    print()
    merdiven_ciz(number3, number1, number2, character1)
    print()
    flama_ciz(number1 + number2 + number3, number3, character2, character1)
    print()
    bayrak_ciz(3 * number3, number2, number3, character1, character2)
    print()
    tek_katli_ev_ciz(number3, number3, character1, character2)
    print()
    apartman_ciz(number2, number1, number3, character1, character2)
    print()
    fiyonk_merdiveni_ciz(2 * number1, number3, character2, character1)


def tamsayi_al(alt_sinir, ust_sinir):
    number = -1
    while number < alt_sinir or number > ust_sinir:
        try:
            number = int(input(f"Enter the number between {alt_sinir} and {ust_sinir}: "))

        except ValueError:
            print("Number must be an integer!")

        else:
            if number < alt_sinir or number > ust_sinir:
                print(f"Number must between {alt_sinir} and {ust_sinir}!")

    return number


def cizim_karakteri_al():
    char = ''
    while len(char) != 1 or (not char.isprintable()) or char.isspace():
        char = input("Enter the printable 1 length character: ")

        if len(char) != 1:
            print("Character must be 1 length!")

        elif not char.isprintable():
            print("Character is not printable!")

        elif char.isspace():
            print("Character is space!")

    return char


def yatay_cizgi_ciz(uzunluk, cizim_karakteri):
    for i in range(uzunluk):
        print(cizim_karakteri, end="")

    print()


def dikdortgen_ciz(dikey_kenar_uzunlugu, yatay_kenar_uzunlugu, cizim_karakteri):
    for i in range(dikey_kenar_uzunlugu):
        for j in range(yatay_kenar_uzunlugu):
            print(cizim_karakteri, end="")

        print()


def kare_ciz(kenar_uzunlugu, cizim_karakteri):
    for i in range(kenar_uzunlugu):
        for j in range(kenar_uzunlugu):
            print(cizim_karakteri, end="")

        print()


def ikizkenar_ucgen_ciz(yukseklik, cizim_karakteri):
    max_length = 2 * yukseklik - 1

    for i in range(1, max_length + 1, 2):
        space_count = int((max_length - i) / 2)

        for j in range(space_count):
            print(" ", end="")

        for k in range(i):
            print(cizim_karakteri, end="")

        for j in range(space_count):
            print(" ", end="")

        print()


def ters_ikizkenar_ucgen_ciz(yukseklik, cizim_karakteri):
    max_length = 2 * yukseklik - 1

    for i in range(max_length, 0, -2):
        space_count = int((max_length - i) / 2)

        for j in range(space_count):
            print(" ", end="")

        for k in range(i):
            print(cizim_karakteri, end="")

        for j in range(space_count):
            print(" ", end="")

        print()


def sag_dik_ucgen_ciz(yukseklik, cizim_karakteri):  # bonus
    for i in range(yukseklik):
        space_count = yukseklik - i - 1

        for j in range(space_count):
            print(" ", end="")

        for k in range(yukseklik - space_count):
            print(cizim_karakteri, end="")

        print()


def ters_dik_ucgen_ciz(yukseklik, cizim_karakteri):  # bonus
    for i in range(yukseklik):
        space_count = i

        for j in range(space_count):
            print(" ", end="")

        for k in range(yukseklik - space_count):
            print(cizim_karakteri, end="")

        print()


def yan_dik_ucgen_ciz(yukseklik, cizim_karakteri1, cizim_karakteri2):  # bonus
    sag_dik_ucgen_ciz(int((yukseklik + 1) / 2), cizim_karakteri1)
    for i in range(int((yukseklik - 1) / 2)):
        space_count = i
        print(" ", end="")
        for j in range(space_count):
            print(" ", end="")

        for k in range(int((yukseklik - 1) / 2) - space_count):
            print(cizim_karakteri2, end="")

        print()


def eskenar_dortgen_ciz(dikey_kosegen_uzunlugu, cizim_karakteri):
    triangle_height = int((dikey_kosegen_uzunlugu + 1) / 2)
    reverse_triangle_height = dikey_kosegen_uzunlugu - triangle_height + 1

    max_length = 2 * reverse_triangle_height - 3

    ikizkenar_ucgen_ciz(triangle_height, cizim_karakteri)

    for i in range(max_length, 0, -2):
        space_count = int((max_length - i) / 2)
        print(" ", end="")

        for j in range(space_count):
            print(" ", end="")

        for k in range(i):
            print(cizim_karakteri, end="")

        for j in range(space_count):
            print(" ", end="")

        print()


def kum_saati_ciz(yukseklik, ust_cizim_karakteri, alt_cizim_karakteri):
    ters_ikizkenar_ucgen_ciz(int(yukseklik / 2), ust_cizim_karakteri)
    ikizkenar_ucgen_ciz(int(yukseklik / 2), alt_cizim_karakteri)


def merdiven_ciz(en_ust_basamak_genisligi, basamak_yuksekligi, basamak_sayisi, cizim_karakteri):
    for i in range(basamak_sayisi):
        length = en_ust_basamak_genisligi + 3 * i
        dikdortgen_ciz(basamak_yuksekligi, length, cizim_karakteri)


def flama_ciz(sopa_uzunlugu, yukseklik, sopa_cizim_karakteri, flama_cizim_karakteri):
    yatay_cizgi_ciz(sopa_uzunlugu, sopa_cizim_karakteri)
    ters_ikizkenar_ucgen_ciz(yukseklik, flama_cizim_karakteri)


def bayrak_ciz(sopa_uzunlugu, dikey_kenar_uzunlugu, yatay_kenar_uzunlugu, sopa_cizim_karakteri, bayrak_cizim_karakteri):
    yatay_cizgi_ciz(sopa_uzunlugu, sopa_cizim_karakteri)
    dikdortgen_ciz(dikey_kenar_uzunlugu, yatay_kenar_uzunlugu, bayrak_cizim_karakteri)


def tek_katli_ev_ciz(cati_yuksekligi, kat_yuksekligi, cati_cizim_karakteri, bina_cizim_karakteri):
    ikizkenar_ucgen_ciz(cati_yuksekligi, cati_cizim_karakteri)
    dikdortgen_ciz(kat_yuksekligi, cati_yuksekligi * 2 - 1, bina_cizim_karakteri)


def apartman_ciz(cati_yuksekligi, kat_yuksekligi, kat_sayisi, cati_cizim_karakteri, bina_cizim_karakteri):
    ikizkenar_ucgen_ciz(cati_yuksekligi, cati_cizim_karakteri)
    for i in range(kat_sayisi):
        dikdortgen_ciz(kat_yuksekligi, 2 * cati_yuksekligi - 1, bina_cizim_karakteri)
        yatay_cizgi_ciz(2 * cati_yuksekligi - 1, cati_cizim_karakteri)


def fiyonk_merdiveni_ciz(fiyonk_yuksekligi, fiyonk_sayisi, ust_cizim_karakteri, alt_cizim_karakteri):
    if fiyonk_sayisi == 0:
        return

    ters_ikizkenar_ucgen_ciz(int(fiyonk_yuksekligi / 2), ust_cizim_karakteri)
    ikizkenar_ucgen_ciz(int(fiyonk_yuksekligi / 2), alt_cizim_karakteri)

    fiyonk_merdiveni_ciz(fiyonk_yuksekligi, fiyonk_sayisi - 1, ust_cizim_karakteri, alt_cizim_karakteri)





if __name__ == '__main__':
    main()
