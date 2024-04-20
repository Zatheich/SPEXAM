from main import HtmlParser
from Logger import *


parser = HtmlParser("https://bank.gov.ua/")
panzer = HtmlParser("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2")
#panther = HtmlParser("https://www.atbmarket.com/product/kartopla-1-gat")
parser.NbuParse('div', 'index-page')
parser.meteoParse( tag= 'div', attribute='index-page')
#parser.KarParse( tag= 'div', attribute='index-page')





try:
    a = input("Cash or tempreture - ")
    if a == "Cash":
        b = input("Euro or Dollars - ")
        logging.info(f"Користувач виконав дію: {a}")
        try:
            if b == "Euro":
                logging.info(f"Користувач виконав дію: {b}")
                digit = float(input("Enter digit: "))
                print(digit * parser.Result[2])
            if b == "Dollars":
                logging.info(f"Користувач виконав дію: {b}")
                digit = float(input("Enter digit: "))
                print(digit * parser.Result[3])
        except TypeError:
            logging.error(f"Помилка: ")
            raise TypeError
    try:
        if a == "tempreture":
            logging.info(f"Користувач виконав дію: {a}")
            print(panzer.Result)
    except TypeError:
        logging.error(f"Помилка: ")
        raise TypeError






except TypeError:
    logging.error(f"Помилка: ")
    raise TypeError
