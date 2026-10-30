word_1 = input("Первое слово: ")
word_2 = input("Второе слово: ")

myset_1 = set(word_1)
myset_2 = set(word_2)

common_letters = myset_1.intersection(myset_2)
print("Буквы в обоих словах:", common_letters)

only_first = myset_1 - myset_2
print("Буквы только в первом:", only_first)

only_second = myset_2 - myset_1
print("Буквы только во втором:", only_second)

all_letters = myset_1.union(myset_2)
print("Все буквы:", all_letters)