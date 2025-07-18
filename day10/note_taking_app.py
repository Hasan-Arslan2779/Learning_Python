#! Dosya İşlemleri
# Dosya açma, okuma ve yazma işlemleri
# Dosya açma: open("dosya_adı", "mod")
# Dosya okuma: read(), readline(), readlines()
# Dosya yazma: write(), writelines()
# Dosya kapatma: close()
# Dosya modları:
# "r" - Okuma modu (varsayılan)
# "r+" - Okuma ve yazma modu (dosya varsa açılır, yoksa hata verir)
# "w+" - Okuma ve yazma modu (varsa dosyayı siler
# "w" - Yazma modu (varsa dosyayı siler)
# "a+" - Ekleme ve okuma modu (varsa dosyayı silmez, dosya yoksa oluşturur)
# "a" - Ekleme modu (varsa dosyayı silmez)
# "b+" - İkili okuma ve yazma modu (binary read/write)
# "b" - İkili mod (binary)
# "x" - Oluşturma modu (varsa dosya oluşturulamaz)
# "x+" - Oluşturma ve okuma modu (varsa dosya oluşturulamaz)
# with open("day10/notes.txt", "r") as file:
#     content = file.read()
# print(content)
# with open("day10/notes1.txt", "w") as file:
#     user = input("Bir şeyler yazın: ")
#     file.write(user)
# print("Dosya başarıyla güncellendi.")
# Dosya içeriğini okuma
# with open("day10/notes1.txt", "r") as file:
#     content = file.read()
# print("Dosya içeriği:", content)

# Dosya ekleme
# with open("day10/notes1.txt", "a") as file:
#     user = input("Dosyaya eklemek istediğiniz metni girin: ")
#     file.write("\n" + user)

# ?  Note Alma Uygulaması
# * 1.Adım :Dosya Adını Tanımlama
FİLE_NAME = "day10/my_notes.txt"

# * 2.Adım :Menü seçeneklerini gösterme


def show_menu():
    print("\n--- Not Alma Uygulaması ---")
    print("Lütfen bir seçenek girin:")
    print("1. Not Ekle")
    print("2. Notları Görüntüle")
    print("3. Notları Sil")
    print("4. Çıkış")

 # * 3.Adım :Not Ekleme İşlemi


def add_note():
    note = input("Notunuzu girin: ")
    with open(FİLE_NAME, "a") as file:
        file.write(note + "\n")
    print("Not başarıyla eklendi.")


# * 4.Adım :Notları Görüntüleme İşlemi
def view_notes():
    try:
        with open(FİLE_NAME, "r") as file:
            notes = file.read()
        if notes:
            print("\n--- Notlar ---")
            print("-", notes)
        else:
            print("Henüz not eklenmemiş.")
    except FileNotFoundError:
        print("Not dosyası bulunamadı. Lütfen önce not ekleyin.")

 # * 5.Adım :Notları Silme İşlemi


def delete_notes():
    confirm = input(
        "Tüm notları silmek istediğinize emin misiniz? (E/H): ").strip().upper()
    if confirm == "E":
        with open(FİLE_NAME, "w") as file:
            # file.write("")  # Dosyayı boşaltıyoruz
            pass  # Dosyayı açıp yazma modunda boş bırakıyoruz
        print("Tüm notlar silindi.")
    else:
        print("Silme işlemi iptal edildi.")


# * 6.Adım :Ana Program Döngüsü
def main():
    while True:
        show_menu()
        choice = input("Seçiminizi yapın (1-4): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek girin.")


main()
