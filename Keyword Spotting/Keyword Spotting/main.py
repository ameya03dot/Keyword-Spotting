from flask import Flask, request
import os
#from flask_cors import CORS, cross_origin
from flashtext import KeywordProcessor

#os.putenv('LANG', 'en_US.UTF-8')
#os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
#CORS(app)

def add(extract):
          keyword_processor = KeywordProcessor()
          r = keyword_processor.add_keyword(extract)
          return r

def prediction(text):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keyword('school')
    keywords_found = keyword_processor.extract_keywords(text, span_info=True)
    return keywords_found

@app.route("/predict", methods=['POST'])
#@cross_origin()
def predictRoute():
    data = request.json["text"]
    p = prediction(data)
    print(p)
    print(type(p))
    return {"Keyword": str(p)}

#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=8008, debug=True)