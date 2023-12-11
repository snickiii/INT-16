import re

# данная реализация метода не универсальна и не работает для строки типа "ззадание задание"
# в данном случае результат будет "ЗЗадание Задание"
def title_1(input: str) -> str:
    words = input.split() #список слов, из которых состоит строка
    modified_words = [w[0].upper() + w[1::] for w in words] #список слов, у каждого из которых первая буква становится заглавной
    modified_input = input
    # замена на слова с заглавной буквой в исходной строке
    for i in range(len(modified_words)):
        modified_input = modified_input.replace(words[i], modified_words[i])
    return modified_input # строка, в которой у каждого слова первая буква становится заглавной

# данная реализация подходит для любых строк
def title_2(input: str) -> str:
    input = [part for part in re.split(r'^(\s+)(.*)', input) if part] # создаем список из последоваетльности пробелов в начале строки и оставяшейся части строки
    if len(input) == 1: # первый случай: в начале строки нет пробелов
        words = re.findall(r'\S+\s*', input[0]) # делим строку на части, состоящие из слова и последовательности пробелов до следующего слова (# элементы списка: "слово_1    ", "слово_2 ", "слово_3" и т.п.)
        return ''.join(word[0].upper() + word[1::] for word in words) # строка, в которой у каждого слова первая буква становится заглавной
    else: # второй случай: строка начинается с последовательности пробелов
        words = re.findall(r'\S+\s*', input[1]) # список с элементами вида: "слово_1    ", "слово_2 ", "слово_3" и т.п.
        return input[0] + ''.join([word[0].upper() + word[1::] for word in words]) # строка, в которой у каждого слова первая буква становится заглавной

def main():
    input_1 = "тесТОвое задание для pt"
    print(f'Исходная строка: {input_1}')
    print(f'1 способ: {title_1(input=input_1)}')
    print(f'2 способ: {title_2(input=input_1)}')

    input_2 = "   тесТОвое ззадание задание  для pt"
    print(f'Исходная строка: {input_2}')
    print(f'1 способ: {title_1(input=input_2)}')
    print(f'2 способ: {title_2(input=input_2)}')

if __name__ == "__main__":
    main()