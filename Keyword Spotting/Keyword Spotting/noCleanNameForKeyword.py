from flashtext import KeywordProcessor

#keyword_processor = KeywordProcessor()
#keyword_processor.add_keyword('Apple pie')
#keyword_processor.add_keyword('childhood')
#keywords_found = keyword_processor.extract_keywords('In my Childhood, i love to eat apple pie.')
#print(keywords_found)

class noCleanName:

    def __init__(self, text, add_keyword):
        self.text = text
        self.add_keyword = add_keyword

    def Findkeywords(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword(self.add_keyword)
        keywords_found = keyword_processor.extract_keywords(self.text)
        return keywords_found

Extract = noCleanName("In my Childhood, i love to eat apple pie." , "Apple pie")
result = Extract.Findkeywords()
print(result)