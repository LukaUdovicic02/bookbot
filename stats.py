def get_num_words(txt):
    return len(txt.split())

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
    return sorted_list

def sort_num(char_dict):
    sorted_list = []
    for key,val in char_dict.items():
        if key.isalpha():
            sorted_list.append({"char": key, "num":val}) 
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]