from main import HtmlParser
from Logger import *


parser = HtmlParser("https://bank.gov.ua/")
panzer = HtmlParser("https://meteo.ua/ua/34/kiev")
parser.NbuParse('div', 'index-page')
parser.meteoParse( tag= 'div', attribute='weather-detail__main-temp')






try:
    a = input("Cash or tempreture - ")
    if a == "Cash":
        b = input("Euro or Dollars - ")
        logging.info(f"Користувач виконав дію: {a}")
        try:
            if b == "Euro":
                logging.info(f"Користувач виконав дію: {b}")
                digit = float(input("Enter digit: "))
                d = digit * parser.Result[2]
                print(d)
                logging.info(f"результат дії: {d}")
            if b == "Dollars":
                logging.info(f"Користувач виконав дію: {b}")
                digit = float(input("Enter digit: "))
                c = digit * parser.Result[3]
                print(c)
                logging.info(f"результат дії: {c}")
        except TypeError as e:
            print("Type Error")
            logging.error(f"Помилка: {e}")
            raise TypeError
    elif a == "tempreture":
        logging.info(f"Користувач виконав дію: {a}")
        print(panzer.Result)
    else:
        raise TypeError(f"Wrong data - {a}")
except TypeError as te:
    msg = f"Помилка: {te}"
    print(msg)
    logging.error(msg)
print("End")