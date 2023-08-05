def apper_text(text):
    new_list = []
    list_of_text = text.split(" ")
    for word in list_of_text:
        new_list.append(word.upper())

    return " ".join(new_list)

