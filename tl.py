import languages
from utils import getTexts

from textblob import TextBlob
from ISO639_2 import ISO639_2
from translate import Translator

class Language:

    def __init__(self, text):
        self.text = text
        self.detect_language()

    def detect_language(self):
        blob = TextBlob(" "+self.text+" ")
        print(blob.detect_language())
        language_code = blob.detect_language()
        if language_code == "zh-CN":
            self.lang_code = "zh"
        else:
            self.lang_code = language_code

    def get_language(self):
        return ISO639_2[self.lang_code], self.lang_code

    def get_translation(self, to="en"):
        translator = Translator(from_lang = self.lang_code, to_lang = to)
        translated_text = translator.translate(self.text)

        return translated_text

    def get_romanization(self):
        romanized_text = getTexts(self.text, self.lang_code)

        return romanized_text


text = "자존심 상해 애가 타"

l = Language(text)
#print(l.get_language())
print(l.get_romanization())
