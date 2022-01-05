import numpy
from korean_romanizer.romanizer import Romanizer as kr_rom #korean
from xpinyin import Pinyin #chinese
from cutlet import Cutlet #japanese
from pythainlp.transliterate import romanize as thai_rom #thai
import cyrtranslit as cyr #russian
from indic_transliteration import sanscript #indic

from translate import Translator

#Korean
def korean(text):
    r = kr_rom(text)
    romanized_text = r.romanize()

    translator = Translator(from_lang = "korean", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Chinese
def chinese(text):
    p = Pinyin()
    romanized_text = p.get_pinyin(text)

    translator = Translator(from_lang = "zh", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Japanese
def japanese(text):
    katsu = Cutlet()
    romanized_text = katsu.romaji(text)

    translator = Translator(from_lang = "japanese", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Thai
def thai(text):
    romanized_text = thai_rom(text)

    translator = Translator(from_lang = "thai", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Russian
def russian(text):
    romanized_text = cyr.to_latin(text, "ru")

    translator = Translator(from_lang = "ru", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Bengali
def bengali(text):
    romanized_text = sanscript.transliterate(text, sanscript.BENGALI, sanscript.ITRANS)

    translator = Translator(from_lang = "bengali", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Hindi
def hindi(text):
    romanized_text = sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)

    translator = Translator(from_lang = "hindi", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Tamil
def tamil(text):
    romanized_text = sanscript.transliterate(text, sanscript.TAMIL, sanscript.ITRANS)

    translator = Translator(from_lang = "tamil", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text

#Telugu
def telugu(text):
    romanized_text = sanscript.transliterate(text, sanscript.TELUGU, sanscript.ITRANS)

    translator = Translator(from_lang = "telugu", to_lang = "english")
    translated_text = translator.translate(text)

    return romanized_text, translated_text
