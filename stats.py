def get_num_words(txt):
    fico = txt.split()
    ficolen = len(fico)
    return print(f"{ficolen} words found in the document")

def get_num_chars(txt):
    text_lower = txt.lower()
    char_dict = {}
    num_chars = 1
    for letter in text_lower:
        if letter in char_dict:
           char_dict[letter] += num_chars
        elif letter not in char_dict: 
            char_dict[letter] = num_chars

    print(char_dict)
    