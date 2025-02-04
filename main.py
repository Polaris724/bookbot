def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()


    #print(text)
    
    word_count = len(text.split())
    print(word_count)

    characters = {}
    text = text.lower()

    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters.update({char:1})
     #print(characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document/n")
    
    for char in characters:
        if char.isalpha():
            

    for
        print(f"The '{}' character was found {} times")


main()