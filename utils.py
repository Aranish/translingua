import languages

# lang = {
#     "ko" : languages.korean(text),
#     # "zh" : languages.chinese(text),
#     # "ja" : languages.japanese(text),
#     # "th" : languages.thai(text),
#     # "ru" : languages.russian(text),
#     # "bn" : languages.bengali(text),
#     # "hi" : languages.hindi(text),
#     # "ta" : languages.tamil(text),
#     # "te" : languages.telugu(text)
# }

def getTexts(text, lang):
    if lang == "ko":
        rom = languages.korean(text)
    elif lang == "zh":
        rom = languages.chinese(text)
    elif lang == "ja":
        rom = languages.japanese(text)
    elif lang == "th":
        rom = languages.thai(text)
    elif lang == "ru":
        rom = languages.russian(text)
    elif lang == "bn":
        rom = languages.bengali(text)
    elif lang == "hi":
        rom = languages.hindi(text)
    elif lang == "ta":
        rom = languages.tamil(text)
    elif lang == "te":
        rom = languages.telugu(text)
    else:
        rom = ""

    return rom
