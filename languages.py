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
    romanized_text = r.romanize()

    return romanized_text

#Chinese
def chinese(text):
    p = Pinyin()
    romanized_text = p.get_pinyin(text)

    return romanized_text

#Japanese
def japanese(text):
    katsu = Cutlet()
    romanized_text = katsu.romaji(text)

    return romanized_text

#Thai
def thai(text):
    romanized_text = thai_rom(text)

    return romanized_text

#Russian
def russian(text):
    romanized_text = cyr.to_latin(text, "ru")

    return romanized_text

#Bengali
def bengali(text):
    romanized_text = sanscript.transliterate(text, sanscript.BENGALI, sanscript.ITRANS)

    return romanized_text

#Hindi
def hindi(text):
    romanized_text = sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)

    return romanized_text

#Tamil
def tamil(text):
    romanized_text = sanscript.transliterate(text, sanscript.TAMIL, sanscript.ITRANS)

    return romanized_text

#Telugu
def telugu(text):
    romanized_text = sanscript.transliterate(text, sanscript.TELUGU, sanscript.ITRANS)

    return romanized_text
