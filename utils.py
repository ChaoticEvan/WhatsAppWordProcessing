symbols_to_remove = [",", "."]
words_to_remove = ["really", "oh", "go", "out", ".com", "www.", "lol", "know", "yeah"]

def process_line(line):
    split_idx = line.find("-")
    message_with_name = line[split_idx + 2:]
    
    name_split_idx = message_with_name.find(":")
    name = message_with_name[:name_split_idx]
    message = message_with_name[name_split_idx:]
    if "Media omitted" in message:
        return name, ""

    message = message.lower()
    message = remove_symbols(message)
    message = remove_common_words(message)    
    return name, remove_common_words(message)

def remove_symbols(message):
    for symbol in symbols_to_remove:
        message = remove_word(message, symbol)
        
    return message

def remove_common_words(message):
    for word in words_to_remove:
        message = remove_word(message, word)

    return message

def remove_word(message, word):
    while word in message:
        message = message.replace(word, "")
    return message