from main import HtmlParser
from Logger import *


parser = HtmlParser("https://bank.gov.ua/")
parser2 = HtmlParser("https://sinoptik.ua/")
parser.NbuParse('div', 'index-page')
parser.meteoParse( tag= 'div', attribute='index-page')





try:
    a = input("Cash or tempreture - ")
    if a == "Cash":
        b = input("Euro or Dollars - ")
        if b == "Euro":
            digit = float(input("Enter digit: "))
            print(digit * parser.Result[2])
        if b == "Dollars":
            digit = float(input("Enter digit: "))
            print(digit * parser.Result[3])
        if b != "Euro":
            logging.error(f"Помилка:")
            raise TypeError
        if b != "Dollars":
            logging.error(f"Помилка:")
            raise TypeError
    if a == "tempreture":
        print(parser.Result)
    if a != "tempreture":
        logging.error(f"Помилка: ")
        raise TypeError




except TypeError as e:
    print("Type Error")
    logging.error(f"Помилка: {e}")
    raise TypeError
