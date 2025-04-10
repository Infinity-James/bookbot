from stats import get_num_words

def frankenstein_word_count():
    try:
        with open('books/frankenstein.txt', 'r') as file:
            contents = file.read()
        return get_num_words(contents)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred: ", e)

def frankenstein_character_frequencies():
    try:
        with open('books/frankenstein.txt', 'r') as file:
            contents = file.read()
        characters = list(contents)
        character_counts: dict[str, int] = {}
        for character in characters:
            lower_character = character.lower()
            if lower_character == ' ' or lower_character == '\n':
                continue
            elif lower_character in character_counts:
                character_counts[lower_character] += 1
            else:
                character_counts[lower_character] = 1
        return character_counts

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred: ", e)
    
word_count = frankenstein_word_count()
character_frequencies = frankenstein_character_frequencies()
sorted_characters = sorted(character_frequencies.items(), key=lambda item: item[1], reverse=True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")

for char, count in sorted_characters:
    print(f"The '{char}' character was found {count} times")