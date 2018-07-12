from loggerConfig import logging
from authentication.authenticate import authenticate

logger = logging.getLogger(__name__)

@authenticate(passwordLength=12)
def addUser(user, client):
   """ This method puts user in database """
   client.setItem(user['username'], user)
   logger.info("User successfully added to db")
