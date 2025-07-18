# Tuples:
# Tupllar değişken sabit uzunlukta ve değiştirilemez (immutable) veri yapılarıdır.
# Tupllar, parantez içinde virgülle ayrılmış değerlerden oluşur.
# Tupllar, genellikle sabit veri kümelerini temsil etmek için kullanılır.
# Tupller listelerden daha hafif ve hızlıdır, çünkü değiştirilemezler.
# my_tuple = (1, 2, 3, 4, 5)
# # Tupllar, listeler gibi indekslenebilir ve dilimlenebilir.
# fruits = ("apple", "banana", "cherry")
# print(fruits[0])  # Çıktı: apple
# Tuplar, listeler gibi döngü ile gezilebilir.
# for fruit in fruits:
#     print(fruit)
# # Tuplar, listeler gibi birleştirilebilir.
# more_fruits = ("orange", "grape")

# coordinates = (10.5, 20.3)
# # Tuplar, birden fazla değişkenle aynı anda ayrıştırılabilir.
# x, y, z = coordinates
# # print(coordinates[0])  # Çıktı: 10.5

# fruits = ("apple", "banana", "cherry")

# print(fruits + ("orange", "grape"))  # Bu şekilde  Tupları birleştirir


# Stler= Kümeler, benzersiz öğelerden oluşan ve sırasız (unordered) veri yapılarıdır.
# Kümeler, süslü parantezler içinde virgülle ayrılmış değerlerden oluş
# Kümeler, matematiksel küme işlemleri için kullanılır.
# Kümeler yinelenen öğeleri otomatik olarak kaldırır.
# my_set = {1, 2, 3, 4, 5}

# malzemeler = {"un", "şeker ", "yumurta", "süt"}
# print(malzemeler)

# # Kümelere öğe eklemek için add() metodu kullanılır.
# malzemeler.add("vanilya")
# print(malzemeler)
# # Kümelerden öğe kaldırmak için remove() veya discard() metodu kullanılır.
# malzemeler.remove("şeker ")
# print(malzemeler)
# # discard() metodu, öğe bulunamazsa hata vermez.
# malzemeler.discard("şeker ")
# print(malzemeler)

# Kümelrede birleştirme işlemi için union() veya | operatörü kullanılır.
# set_a = {"un", "şeker", "yumurta"}
# set_b = {"süt", "şeker"}

# print(set_a.union(set_b))  # union() metodu ile birleştirme
# print(set_a | set_b)        # | operatörü ile birleştirme
# # Kümelerde kesişim işlemi için intersection() veya & operatörü kullanılır.
# print(set_a.intersection(set_b))  # intersection() metodu ile kesişim
# print(set_a & set_b)                # & operatörü ile kesişim
# # Kümelerde fark işlemi için difference() veya - operatörü kullanılır.
# # bir kümede olup diğerinde olmayan elemanları döndürür.
# print(set_a.difference(set_b))  # difference() metodu ile fark
# print(set_a - set_b)              # - operatörü ile fark

#! MALZEME KONTROLCÜSÜ
#
# *  1.Adım :Yemek Tarifi Malzemeleri
recipe_ingredients = {
    "un",
    "şeker",
    "yumurta",
    "süt",
    "vanilya",
}
# * Adım 2: Kullanıcıdan Malzeme Girişi
user_input = input("Lütfen malzeme adını girin (virgülle ayrılacak): ")
# Kullanıcının girdiği malzemeleri küme olarak alıyoruz
user_ingredients = set(user_input.split(","))

# * Adım 3: Malzeme Kontrolü
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# * Adım 4: Sonuçları Yazdırma
print("\nMalzeme Kontrol Sonuçları:")

if missing_ingredients:
    print(
        f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the required ingredients.")
if extra_ingredients:
    print(
        f"You have extra ingredients that are not needed: {', '.join(extra_ingredients)}")
else:
    print("You have no extra ingredients.")
