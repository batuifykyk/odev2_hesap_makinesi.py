"""
Ödev 2 – if ile Temel Hesap Makinesi
Açıklama: Kullanıcıdan alınan iki sayı ve operatör ile 6 temel aritmetik işlemi 
if / elif / else koşul yapılarıyla gerçekleştirebilen bir program.
"""

def main():
    # 1. Kullanıcıdan iki sayı alınması (ondalıklı olabileceği için float kullanılır)
    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    # 2. İşlem operatörünün alınması
    operator = input("İşlemi giriniz (+, -, *, /, **, //): ").strip()

    # 3. ve 5. Koşul yapılarıyla işlemlerin ve sıfıra bölme kontrollerinin yapılması
    if operator == "+":
        sonuc = sayi1 + sayi2
        print(f"Sonuç: {sonuc}")
    elif operator == "-":
        sonuc = sayi1 - sayi2
        print(f"Sonuç: {sonuc}")
    elif operator == "*":
        sonuc = sayi1 * sayi2
        print(f"Sonuç: {sonuc}")
    elif operator == "/":
        if sayi2 == 0:
            print("Hata: Bir sayı sıfıra bölünemez.")
        else:
            sonuc = sayi1 / sayi2
            print(f"Sonuç: {sonuc}")
    elif operator == "**":
        sonuc = sayi1 ** sayi2
        print(f"Sonuç: {sonuc}")
    elif operator == "//":
        if sayi2 == 0:
            print("Hata: Bir sayı sıfıra bölünemez.")
        else:
            sonuc = sayi1 // sayi2
            print(f"Sonuç: {sonuc}")
    else:
        # 6. Listelenmeyen bir operatör girildiğinde verilecek uyarı
        print("Bilinmeyen işlem")


if __name__ == "__main__":
    main()
