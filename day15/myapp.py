# Pythonda Dosya Okuma İşlmei
# with open("day15/sample.txt", "r") as file:
#     content = file.read()
#     print(content)


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
# Dosyanın içeriğini satır satır okumak için
# with open("day15/sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # strip() ile satır sonu karakterlerini kaldırıyoruz

# try:
#     with open("day15/samples.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Dosya bulunamadı. Lütfen dosya yolunu kontrol edin.")

# ? Tarif Görüntüleme Uygulaması
# 1. Adım Tarfileri Dosyadan yükleme
def load_recipes(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            recipes = content.split("\n\n")
        recipes_dict = {}
        for recipe in recipes:
            lines = recipe.strip().split("\n")
    except FileNotFoundError:
        print("Tarif dosyası bulunamadı.")
        return []
