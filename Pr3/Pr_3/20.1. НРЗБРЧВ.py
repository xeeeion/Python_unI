translatedText = " "

def translate(text):
    global translatedText
    letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-']
    for i in range(len(text) - 1):
        if letters.count(text[i]) == 0:
            translatedText = translatedText + text[i]
    translatedText = " ".join(translatedText.split())
    return translatedText
