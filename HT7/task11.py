from collections import Counter
import re


def most_common_words_from_file(file_path, num_words=1):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        most_common = word_counts.most_common(num_words)

        return most_common


file_path = 'Files/11.txt'
result = most_common_words_from_file(file_path, num_words=5)

if result:
    print("Самые встречающиеся слова:")
    for word, count in result:
        print(f"{word}: {count}")
