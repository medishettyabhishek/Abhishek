from _pytest import logging

class baseclass:
    def test_loggingDemo(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.CRITICAL)
        return logger

