from golive.utils.utils import *
from golive.active_users.based_on_app_in.based_on_app_in_purchases import *

coins = int(sys.argv[1])
activeUsers = []
data = findDataFromApplication('./golive/data/app_in.json', "Data")
usersdata = findDataOfEachUser(data)

for i in usersdata:
	isNumSessions = processDataOfUser(usersdata[i], coins)
	if(isNumSessions):
		activeUsers.append(i)

outputListOfActiveUsers(activeUsers,coins)
