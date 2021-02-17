from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('corona virus', 'Italy')
keyword_processor.add_keyword('China')
keywords_found = keyword_processor.extract_keywords('913 deaths because of corona virus in a day in Italy, and China have lost 5 today.')
print(keywords_found)