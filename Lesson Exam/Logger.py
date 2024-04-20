from logging import *

import logging


class Logger:
    logging.basicConfig(filename='errors.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    def __init__(self, loggerName: str, level: int = DEBUG, fileName: str = "loggingFile.log", ):
        self.Level = level
        self.__Configure(loggerName, fileName)

    def __Configure(self, loggerName: str, fileName: str):
        self.__Logger = logging.getLogger(loggerName)
        self.__Logger.setLevel(self.Level)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s - %(name)s - %(message)s")
        file_handler = logging.FileHandler(fileName, 'a')
        file_handler.setFormatter(formatter)
        self.__Logger.addHandler(file_handler)

    def __Log(self, message: str):
        try:
            if (message is None or message == ""):
                raise TypeError("Value cannot be None or ")
            if self.Level == DEBUG:
                self.__Logger.debug(message)
            if self.Level == INFO:
                self.__Logger.info(message)
            if self.Level == WARNING:
                self.__Logger.warning(message)
            if self.Level == ERROR:
                self.__Logger.error(message)
            if self.Level == CRITICAL:
                self.__Logger.critical(message)
        except Exception as ex:
            self.__Logger.critical(ex)
            logging.error(f"Помилка: {ex}")
            raise ex

    def __LogDecorator(self, *exc_types):
        def Decorator(function):
            def Wrapper(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (exc_types) as ex:
                    logging.error(f"Помилка: {ex}")

                    raise ex

            return Wrapper

        return Decorator

    @__LogDecorator(Exception)
    def Log(self, message: str):
        try:
            self.__Log(message)
        except:
            raise