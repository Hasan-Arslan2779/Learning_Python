# ! Modüller Ve Kütüphanaler
# mödüller, Python'da kodunuzu daha modüler ve yeniden kullanılabilir hale getirmek için kullanılır. Kütüphaneler ise genellikle belirli bir işlevselliği sağlamak için bir araya getirilmiş modüllerdir.
# import math
# print(math.sqrt(24)) # karekök almak için kullanılır

# from random import choice
# import random
# print(random.randint(1, 5))

# print(choice(["apple", "banana", "cherry"]))

# import random
# password = "".join(random.choices(
#     "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))
# print(f"Generated Password: {password}")
# ? Özel modüller ve kütüphaneler oluşturma

# import greetings

# print(greetings.sayHello("Hasan"))  # "Hello, Hasan!" çıktısını verir

import random
import string


def generate_password(length=8):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Karakter kümeleri şifreleme için kullanılır
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Karakter kümelerinden en az birer tane seçilir
    password_characters = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Kalan karakterler rastgele seçilir
    all_characters = uppercase + lowercase + digits + special_characters
    password_characters += random.choices(all_characters, k=length - 4)

    # Karakterler karıştırılır ve şifre oluşturulur
    random.shuffle(password_characters)

    return "".join(password_characters)


try:
    length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(f"Error: {e}")
