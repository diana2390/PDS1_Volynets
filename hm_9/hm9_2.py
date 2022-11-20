class TextProcessor:
    _punktuation = '.,!?;:*'
    @classmethod
    def __is_punktuation(cls, sym):
        return sym in cls._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for sym in text:
            if self.__is_punktuation(sym):
                continue
            clean_text += sym
        return clean_text
class TextLoader:
    __text_processor = TextProcessor()
    __clean_string = None
    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)
    @property
    def clean_string(self):
        print(f"Clean text is: {self.__clean_string}")
        return self.__clean_string
class DataInterface:
    __text_loader = TextLoader()
    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_text(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts

data_i = DataInterface()
text = ["I eat pizza: for dinner?", "and drink some coffee**!"]
clean_text = data_i.process_texts(text)

