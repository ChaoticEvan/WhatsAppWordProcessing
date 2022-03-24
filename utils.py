def process_line(line):
    split_idx = line.find("-")
    message_with_name = line[split_idx + 2:]
    
    name_split_idx = message_with_name.find(":")
    message = message_with_name[name_split_idx:]
    return message