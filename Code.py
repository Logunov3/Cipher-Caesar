def encrypt(s, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s = s.upper()
    result = ''
    lenght = len(letters)

    for letter in s:
        if letter in letters:
            index = letters.find(letter)
            result += letters[(index + k) % lenght]
        else:
            result += letter
    return result


slovo = input('Введите предложение: ')
step = int(input('Введите шаг: '))
print(encrypt(slovo, step))