def check_rhythm(poem):
    lines = poem.split()
    syllables = []
    for line in lines:
        words = line.split('-')
        syllable_count = sum(
            1 for word in words for char in word if char.lower() in 'aeiouаеёиоуыэюя')
        syllables.append(syllable_count)

    if all(syllable == syllables[0] for syllable in syllables):
        return "Парам пам-пам"
    else:
        return "Пам парам"


poem = input("Введите стихотворение: ")
result = check_rhythm(poem)
print(result)
