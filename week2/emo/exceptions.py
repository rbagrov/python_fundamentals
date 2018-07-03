# This file contains custom exception classes

class CustomBaseException(Exception):
    """ This is a base class for all custom exceptions """
    def __init__(self,  logger, *args):
        self.logger = logger
        Exception.__init__(self, *args)

    def logg_error(self, msg):
        self.logger.error(msg)

    def logg_warning(self, msg):
        self.logger.warning(msg)

    def logg_info(self, msg):
        self.logger.info(msg)

    def logg_debug(self, msg):
        self.logger.debug(msg)

    def logg_critical(self, msg):
        self.logger.critical(msg)

class InvalidTextError(CustomBaseException):
    """ This is a custom exceptions for invalid text errors  """
    def __init__(self, logger):
        super(InvalidTextError, self).__init__(logger)

class CurseWordsWarning(CustomBaseException):
    """ This is a custom exception for bad words """
    def __init__(self, logger):
        super(CurseWordsWarning, self).__init__(logger)

class SensetiveDataWarning(CustomBaseException):
    """ This is a custom exception for sensetive data """
    def __init__(self, logger):
        super(SensetiveDataWarning, self).__init__(logger)

class InvalidFileError(CustomBaseException):
    """ This is a custom exception for invalid files """
    def __init__(self, logger):
        super(InvalidFileError, self).__init__(logger)