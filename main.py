#Создаём списки для проверки 
str_consonants = "бвгджзйклмнпрстфхцчшщ"
str_vowel = "аеёиоуыэюя"
#Счетчик согласных букв
consonants = 0  
#Счетчик гласных букв
vowel = 0    
string = input("Введите строку для вывода количества согласных и гласных букв и её длины:")
#Подсчет длины строки
str_len = len(string)
#Приводим строку к нижнему регистру
for i in string.lower():  
    if i in str_vowel:
       vowel += 1
    elif i in str_consonants:
       consonants += 1
#Вывод результата
print(f"Количество согласных букв в строке равно: {consonants}, количество гласных букв в строке равно: {vowel} длина строки равна: {str_len}")
