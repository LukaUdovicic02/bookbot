def get_num_words(txt):
    fico = txt.split()
    ficolen = len(fico)
    return print(f"Found {ficolen} total words")

def get_num_chars(txt):
    text_lower = txt.lower()
    char_dict = {}
    num_chars = 1
    for letter in text_lower:
        if letter in char_dict:
           char_dict[letter] += num_chars
        elif letter not in char_dict: 
            char_dict[letter] = num_chars
    sorted_list = sort_num(char_dict)
    
    get_num_words(text_lower)
    for items_dict in sorted_list:
        print(f"{items_dict["char"]}: {items_dict["num"]}")    

def sort_num(char_dict):
    sorted_list = []
    for key,val in char_dict.items():
        sorted_dict = {}
        if key.isalpha():
            sorted_dict["char"] = key
            sorted_dict["num"] = val
            sorted_list.append(sorted_dict) 
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]