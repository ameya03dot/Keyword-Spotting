from flashtext import KeywordProcessor

#keyword_processor = KeywordProcessor()
#keyword_dict = {
#     "python": ["python", "python programing"],
#     "senior developer": ["SD", "python developer"]}
# {'clean_name': ['list of unclean names']}
#keyword_processor.add_keywords_from_dict(keyword_dict)
# Or add keywords from a list:
#keyword_processor.add_keywords_from_list(["pearl", "python"])
#extractedKeyword = keyword_processor.extract_keywords('I am a SD of python programing')
#print(extractedKeyword)


class addMultikeywords:

     def __init__(self, text, keyword_dict):
          self.text = text
          self.keyword_dict = keyword_dict

     def addkey(self):
          keyword_processor = KeywordProcessor()
          keyword_processor.add_keywords_from_dict(self.keyword_dict)
          extractedKeyword = keyword_processor.extract_keywords(self.text)
          return extractedKeyword


adding = addMultikeywords("I am a SD and my speciality is python programming." , {"python": ["python", "python programing"],"senior developer": ["SD", "python developer"]})
result = adding.addkey()
print(result)
