import logging

from exceptions import InvalidTextError, CurseWordsWarning, SensetiveDataWarning, InvalidFileError

# Create and configure logger could be exctracted in a seperate config file (new task? )

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger(__name__)

# Test raise the new exceptions

try:
    raise InvalidTextError(logger)
except InvalidTextError as error:
    error.logg_error("text contains invalid symbols")

try:
    raise CurseWordsWarning(logger)
except CurseWordsWarning as warning:
    warning.logg_warning("This text contains bad words")

try:
    raise SensetiveDataWarning(logger)
except SensetiveDataWarning as warning:
    warning.logg_warning("This text contains sensative data such as company name")

try:
    raise InvalidFileError(logger)
except InvalidFileError as error:
    error.logg_error("This file is invalid")
