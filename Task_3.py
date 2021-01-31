import string

ENCODING = 'UTF-8'


def remove_punctuation(in_str):
    for p in string.punctuation:
        in_str.replace(p, '')
    return in_str


def get_words(in_str):
    return remove_punctuation(in_str).split()


def find_count_words(file_name, word):
    sum_w = 0
    with open(file_name, 'r', encoding=ENCODING) as file:
        for line in file:
            list_words = get_words(line)
            sum_w = sum_w + list_words.count(word)
    return sum_w


def run(file_name, word):
    count = find_count_words(file_name, word)
    print("В файле '" + file_name + "' частота вхождения слова '" + word + "' " + str(count))


run("Test.txt", "Иван")