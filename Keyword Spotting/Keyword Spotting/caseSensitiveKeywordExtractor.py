from flashtext import KeywordProcessor

#keyword_processor = KeywordProcessor(case_sensitive=True)
#keyword_processor.add_keyword('corona virus', 'Italy')
#keyword_processor.add_keyword('china')
#keywords_found = keyword_processor.extract_keywords('913 deaths because of corona virus in a day in Italy, and China have lost 5 today.')
#print(keywords_found)


class CaseSensitiveKey:
    def __init__(self, text, add_keyword):
        self.text = text
        self.add_keyword = add_keyword

    def keysense(self):
        keyword_processor = KeywordProcessor(case_sensitive=True)
        keyword_processor.add_keyword(self.add_keyword)
        keywords_found = keyword_processor.extract_keywords(self.text)
        return keywords_found


sense = CaseSensitiveKey("913 deaths because of corona virus in a day in Italy, and China have lost 5 today.", 'Italy')
result = sense.keysense()
print(result)

