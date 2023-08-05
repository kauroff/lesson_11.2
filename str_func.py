def apper_text(text):
"""
Функция возвращает текст, написанный капсом
"""
    new_list = []
    list_of_text = text.split(" ")
    for word in list_of_text:
        new_list.append(word.upper())

    return " ".join(new_list)

