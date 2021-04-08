import logging

class Logger:

    def __init__(self):
        self.logger = None
        self.logger = logging.getLogger("__name__")
        self.formater = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
        file_handler = logging.FileHandler("..\\logs\\write_main.log")
        file_handler.setFormatter(self.formater)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formater)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def write_critical(self):
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical("critical msg")

    def write_error(self):
        self.logger.setLevel(logging.ERROR)
        self.logger.error("error message")

    def write_warning(self):
        self.logger.setLevel(logging.WARNING)
        self.logger.warning("warning message")

    def write_info(self):
        self.logger.setLevel(logging.INFO)
        self.logger.info("information")

    def write_debug(self):
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("debug msg")

if __name__=="__main__":
    a = Logger()
    a.write_critical()
    a.write_error()
    a.write_warning()
    a.write_info()
    a.write_debug()