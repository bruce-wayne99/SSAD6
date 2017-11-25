from golive.utils.utils import *
from golive.active_users.based_on_sessions.based_on_sessions import *

sessions = int(sys.argv[1])
activeUsers = []
data = findDataFromApplication('./golive/data/session_data.json', "Data")
usersdata = findDataOfEachUser(data)

for i in usersdata:
	isNumSessions = processDataOfUser(usersdata[i], sessions)
	if(isNumSessions):
		activeUsers.append(i)

outputListOfActiveUsers(activeUsers,sessions)
