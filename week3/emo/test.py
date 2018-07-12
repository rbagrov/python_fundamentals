# This file is used for testing if the add user method works
from addUser import addUser

userA = {'username': "pesho", 'password': "1234"}
userB = {'username': "emo", 'password': "12345678901234"}
userC = {'username': "emo", 'password': "12345678901234"}
userD = {'username': "pesho", 'password': "12345678901234"}

addUser(userA)
addUser(userB)
addUser(userC)
addUser(userD)
