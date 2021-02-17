from flashtext import KeywordProcessor

#kp = KeywordProcessor()
#kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
#kp.add_keyword('Delhi', ('Location', 'Delhi'))
#keywordWithInfo = kp.extract_keywords('Taj Mahal is in Delhi.')
#print(keywordWithInfo)
# [('Monument', 'Taj Mahal'), ('Location', 'Delhi')]
# NOTE: replace_keywords feature won't work with this.


class getExtractinfo:

    def __init__(self, text):
        self.text = text

    def Extract(self):
        kp = KeywordProcessor()
        kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
        kp.add_keyword('Delhi', ('Location', 'Delhi'))
        keywordWithInfo = kp.extract_keywords(self.text)
        return keywordWithInfo

get = getExtractinfo("Taj Mahal is in Delhi.")
result = get.Extract()
print(result)


