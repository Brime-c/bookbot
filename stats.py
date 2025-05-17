def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort(characters):
    sorted = []
    for char, count in characters.items():
        sorted.append({"char": char,"num": count})
    sorted.sort(reverse=True, key=lambda count: count["num"])
    return sorted

        


