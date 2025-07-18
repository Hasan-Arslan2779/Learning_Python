# ! Python İstisna Yönetimi ve Güvenli Hesap Makinesi Uygulaması
# try:
#     num = int(input("Bir sayı girin: "))
#     result = 10 / num
#     print(f"Sonuç: {result}")
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
# except ValueError:
#     print("Geçersiz giriş! Lütfen bir sayı girin.")

# try:
#     # Code that may raise an exception
#     except ExceptionType:
#         # Handle the exception
# else:
#     # Code to execute if no exception occurs
# finally:
#     # Code that will always execute, regardless of exceptions
#     print("Bu kod her zaman çalışır.")

# try:
#     num = int(input("Bir sayı girin: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
# except ValueError:
#     print("Geçersiz giriş! Lütfen bir sayı girin.")
# else:
#     print("İşlem başarılı, hata oluşmadı.")
#     print(f"Sonuç: {result}")
# finally:
#     print("Program sonlandı.")


# Birden fazla istisna türünü yakalamak için birden fazla except bloğu kullanabilirsiniz.
# try:
#     num = int(input("Bir sayı girin: "))
#     result = 10 / num
#     print(f"Sonuç: {result}")
# except (ZeroDivisionError, ValueError) as e:
#     if isinstance(e, ZeroDivisionError):
#         print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
#     elif isinstance(e, ValueError):
#         print("Geçersiz giriş! Lütfen bir sayı girin.")


# ? Özel istisnalar oluşturma
# raise anahtar kelimesi ile özel istisnalar oluşturabilirsiniz.
# def withdraw(amount):
#     if amount <= 0:
#         raise ValueError(
#             "Çekilen miktar sıfırdan büyük olmalıdır- negatif veya sıfır olamaz.")
#     print(f"{amount} TL çekildi.")


# try:
#     withdraw(100)
# except ValueError as e:
#     print(f"Hata: {e}")


# ! Güvenli Hesap Makinesi Uygulaması


# * Adım 1:Hesap Makinesi Fonksiyonunu Tanımlama
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError(
            "Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
    return x / y


# * Adım 2 : Menüyü Gösterme
def show_menu():
    print("\n--- Güvenli Hesap Makinesi ---")
    print("Lütfen bir işlem seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

   # * Adım 3 : Ana Program Döngüsü
while True:
    show_menu()
    choice = input("Seçiminizi yapın (1/2/3/4/5): ")

    if choice == '5':
        print("Hesap makinesi kapatılıyor...")
        break

    try:
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if choice == '1':
            print(f"Sonuç: {add(num1, num2)}")
        elif choice == '2':
            print(f"Sonuç: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Sonuç: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Sonuç: {divide(num1, num2)}")
        else:
            print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
    except ZeroDivisionError as e:
        # Hata mesajını dosyaya yazma
        print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
        if e:
            with open("error_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"{e}\n")
        print(f"Hata: {e}")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

    finally:
        print("Güvenli Hesap Makinesi işlemini kullandığınız için teşekkürler!  Yeniden başlatılıyor...")
