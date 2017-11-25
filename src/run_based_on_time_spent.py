from golive.utils.utils import *
from golive.active_users.based_on_time_spent_on_a_level.time_spent_level import *

level = int(sys.argv[1])
threshold_time = int(sys.argv[2])
activeUsers = []
data = findDataFromApplication('./golive/data/time_spent.json', "Data")

data = modifyUnixTime(data)

data = filter_level(data,level)

usersdata = findDataOfEachUser(data)

usersdata = sortDataBasedOnSessionTime(usersdata)


for i in usersdata:
    isSpend = processDataOfUser(usersdata[i], level, threshold_time)
    if(isSpend):
        activeUsers.append(i)
outputListOfActiveUsers(activeUsers,level,threshold_time)
