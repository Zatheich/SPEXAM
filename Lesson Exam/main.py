import requests as r
from bs4 import BeautifulSoup as bs
class HtmlParser:
    def meteoParse(self, tag, attribute):
        try:
            response = r.get(self.Url)
            markup = response.content
            htmlDoc = bs(markup, features="html.parser")
            tags = htmlDoc.find_all(tag, attrs={'class' : attribute})
            counter = 0
            for tag in tags:
                strValue = tag.text.strip().replace(',', '.')
                self.Result[counter] = float(strValue)
                counter += 1
        except:
            raise
    def __init__(self, url: str):
        self.Url: str = url
        self.Result: dict = dict()
    def NbuParse(self, tag: str, attribute: str):
        try:
            response = r.get(self.Url)
            markup = response.content
            htmlDoc = bs(markup, features="html.parser")
            tags = htmlDoc.find_all(tag, attrs={'class' : attribute})
            counter = 0
            for tag in tags:
                strValue = tag.text.strip().replace(',', '.')
                self.Result[counter] = float(strValue)
                counter += 1
        except:
            raise

