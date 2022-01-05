import languages
from textblob import TextBlob
from ISO639_2 import ISO639_2


class Language:

    def __init__(self, text):
        self.text = text
        self.detect_language()

    def detect_language(self):
        blob = TextBlob(" "+self.text+" ")
        language_code = blob.detect_language()
        if language_code == "zh-CN":
            #return "zh"
            self.lang_code = "zh"
        else:
            self.lang_code = language_code

    def get_language(self):
        return ISO639_2[self.lang_code]
        #return self.lang_code

l = Language("గొప్పది")
print(l.get_language())
