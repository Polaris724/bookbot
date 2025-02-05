def sort_on(dict):
        return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    #print(text) --> If wanting to output the .txt file
    
    word_count = len(text.split())

    characters = {}
    text = text.lower()

    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters.update({char:1})
     #print(characters) -> Debugging for loop

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    char_list = []
    for char, count in characters.items():
        if char.isalpha():
            char_list.append({'name': char, 'num': count})
            
    char_list.sort(reverse=True, key=sort_on)
    for char_dict in char_list:
       print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")
    print("--- End report ---")

main()