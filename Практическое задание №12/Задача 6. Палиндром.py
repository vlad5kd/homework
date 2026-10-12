word = input("Введите слово: ")

chars_list = list(word)

reversed_chars_list = chars_list[::-1]

if chars_list == reversed_chars_list:
    print(f"'{word}' — Это палиндром")
else:
    print(f"'{word}' — Не палиндром")