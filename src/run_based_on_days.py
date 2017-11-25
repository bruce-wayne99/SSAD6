from golive.utils.utils import *
from golive.active_users.based_on_days.based_on_days import *

consec_days = int(sys.argv[1])
session_gap = 2
activeUsers = []

data = findDataFromApplication('./golive/data/session_data.json', "Data")

data = modifyUnixTime(data)

usersdata = findDataOfEachUser(data)

usersdata = sortDataBasedOnSessionTime(usersdata)

for i in usersdata:
    isActive = processDataOfUser(usersdata[i], session_gap, consec_days)
    if(isActive):
        activeUsers.append(i)

outputListOfActiveUsers(activeUsers,consec_days)
