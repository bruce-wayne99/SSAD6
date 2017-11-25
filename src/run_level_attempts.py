from golive.utils.utils import *
from golive.active_users.based_on_level_attempts.level_attempts import *

level = int(sys.argv[1])
attempts_lowerbound = int(sys.argv[2])
attempts_upperbound = int(sys.argv[3])
level_stuck_users = []

data = findDataFromApplication('./golive/data/level_attempts.json', "Data")

data = modifyUnixTime(data)

data = filter_level(data,level)

usersdata = findDataOfEachUser(data)

for i in usersdata:
	if(len(usersdata[i])>=attempts_lowerbound and len(usersdata[i])<=attempts_upperbound):
		level_stuck_users.append(i)


outputListOfLevelStuckUsers(level_stuck_users,attempts_lowerbound,attempts_upperbound,level)
