def apper_text(text):
    """
    Функция возвращает текст, каждая буква которого написана капсом
    """
    new_list = []
    list_of_text = text.split(" ")
    for word in list_of_text:
        new_list.append(word.upper())

    return " ".join(new_list)

def title_text(text):
    """
    Возвращает текст, каждое слово которого начинается с большой буквы
    """
    new_list = []
    list_of_text = text.split(" ")
    for word in list_of_text:
        new_list.append(word.title())

    return " ".join(new_list)

