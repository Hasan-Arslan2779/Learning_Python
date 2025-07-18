# ! LİSTE KAVRAYIŞI

# kareler = [i**2 for i in range(1, 11)]
# print(kareler)

# numbers = [1, 2, 3, 4, 5]
# double = [x * 2 for x in numbers]
# print(double)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)


# names = ["Alice", "Bob", "Charlie", "David"]
# short_names = [name for name in names if len(name) <= 5]
# print(short_names)

# numbers = [1, 2, 3, 4, 5]
# labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
# print(labels)

# ! Öğrenci notlarını liste kavrayışı ile filtreleme

# * Adım 1: Öğrenci notlarını al
sttudents_scores = input(
    "Enter student scores separated by commas: ")
scores = [int(score) for score in sttudents_scores.split(",")]

# * Adım 2: Notları filtrele
grades = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >=
          # buradaki # else if yapısına "elif" denir
          70 else "D" if score >= 60 else "F" for score in scores]


# Adım 3 : Geçen Ve Kalan Öğrencileri Ayır
passed_students = [score for score in scores if score >= 60]
failed_students = [score for score in scores if score < 60]


# * Adım 4: Sonuçları Yazdır
print("\n---Student Grades---")
# zip ile not ve harfleri birleştiriyoruz
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")


print("\n---Passed Students and Failing Students ---")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")
