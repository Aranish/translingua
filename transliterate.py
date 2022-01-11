import numpy
from korean_romanizer.romanizer import Romanizer as kr_rom #korean
from xpinyin import Pinyin #chinese
from cutlet import Cutlet #japanese
from pythainlp.transliterate import romanize as thai_rom #thai
import cyrtranslit as cyr #russian
from indic_transliteration import sanscript #indic



#Korean
def korean(text):
    r = kr_rom(text)
    transliterated_text = r.romanize()

    return transliterated_text

#Chinese
def chinese(text):
    p = Pinyin()
    transliterated_text = p.get_pinyin(text)

    return transliterated_text

#Japanese
def japanese(text):
    katsu = Cutlet()
    transliterated_text = katsu.romaji(text)

    return transliterated_text

#Thai
def thai(text):
    transliterated_text = thai_rom(text)

    return transliterated_text

#Russian
def russian(text):
    transliterated_text = cyr.to_latin(text, "ru")

    return transliterated_text

#Bengali
def bengali(text):
    transliterated_text = sanscript.transliterate(text, sanscript.BENGALI, sanscript.ITRANS)

    return transliterated_text

#Hindi
def hindi(text):
    transliterated_text = sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)

    return transliterated_text

#Tamil
def tamil(text):
    transliterated_text = sanscript.transliterate(text, sanscript.TAMIL, sanscript.ITRANS)

    return transliterated_text

#Telugu
def telugu(text):
    transliterated_text = sanscript.transliterate(text, sanscript.TELUGU, sanscript.ITRANS)

    return transliterated_text
