def process_line(line):
    split_idx = line.find("-")
    message_with_name = line[split_idx + 2:]
    
    name_split_idx = message_with_name.find(":")
    name = message_with_name[:name_split_idx]
    message = message_with_name[name_split_idx:]
    if "Media omitted" in message:
        return name, ""

    return name, remove_common_words(message)

def remove_common_words(message):
    message = message.lower()
    message = message.replace("really", "")
    message = message.replace("oh", "")
    message = message.replace("com", "")
    message = message.replace("www", "")
    return message